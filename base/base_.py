#encoding=utf-8
import json
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from utils.logger import get_logger
from utils.prase_yaml import PraseYaml

class Base:
    _params={}
 #   _driver= None
#    base_url = ""
    _chance_list={(By.XPATH,"//*[@id='lbNormal']")}
    _max=1
    _error=0


    def __init__(self,driver: WebDriver= None):
        self.Log = get_logger()
        self._driver = driver

    def base_find_element(self,type,locator):
        try:
  #          element=self._driver.find_element(type,locator)
            element = WebDriverWait(self._driver, 10).until \
                (lambda x: x.find_element(type, locator))
            return element
        except Exception as e:
            self.Log.error(f"Find {type}:{locator} fail and Exception is {e}")
            if self._error > self._max:
                raise e
            self._error +=1
            for i in self._chance_list:
                element=WebDriverWait(self._driver, 10).until \
                (lambda x: x.find_element(*i))
                element.click()
                return element
            raise e

    def base_click(self,type,locator):
        try:
            self.base_find_element(type,locator).click()
            self.Log.info(f"Click {type}:{locator} successful")
        except Exception as e:
            self.Log.error(f"Click {type}:{locator} fail and Exception is {e}")
            raise e

    def base_scroll_view_click(self,type,locator):
        try:
            time.sleep(3)
            WebDriverWait(self._driver, 5).until(expected_conditions.
                                                 presence_of_element_located((type, locator)))
            self._driver.execute_script("arguments[0].scrollIntoView(true);",
                                       self.base_find_element(type,locator))
            time.sleep(3)
            self.base_find_element(type, locator).click()
            self.Log.info(f"Scroll view click {type}:{locator} successful")
        except Exception as e:
            self.Log.error(f"Scroll view click {type}:{locator} fail and Exception is {e}")
            raise e

    def base_sendKeys(self,type,locator,value):
        try:
            self.base_find_element(type,locator).send_keys(value)
            self.Log.info(f"SendKeys {type}:{locator} successful")
        except Exception as e:
            self.Log.error(f"SendKeys {type}:{locator} fail and Exception is {e}")
            raise e

    def base_get_text(self,type,locator):
        try:
            text = self.base_find_element(type, locator).text
 #           text=self.base_find_element(type, locator).get_attribute('textContent')
            self.Log.info(f"get_text {type}:{locator} successful")
            return text
        except Exception as e:
            self.Log.error(f"get_text {type}:{locator} fail and Exception is {e}")
            return None

    def excute_scrollTop(self):
        time.sleep(2)
        self._driver.execute_script("document.documentElement.scrollTop=100")
        time.sleep(2)

    def steps(self, file_path):
        steps = PraseYaml.get_yaml_name(file_path)
        raw = json.dumps(steps)
        for key,value in self._params.items():
            raw=raw.replace(f'${{{key}}}',value)
        steps = json.loads(raw)
#        self.Log.info(f"------{steps}")
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    self.base_click(step["by"], step["locator"])
                if action == "baseScrollClick":
                    self.base_scroll_view_click(step["by"], step["locator"])
                if action == "sendkeys":
                    self.base_sendKeys(step["by"], step["locator"],step['input'])
                if action == "frame|0":
                    self._driver.switch_to.frame(0)


    def verify_steps(self,validate):
        result = False
        self.Log.info(f"Start Verify yaml:{validate}")
        if "action" in validate.keys():
            action = validate["action"]
            if action.split("|")[0] == "text" and action.split("|")[1] == "equal":
                actual_text = self.base_get_text(validate["by"], validate["locator"])
                self._driver.get_screenshot_as_file("temp.PNG")
                with open("temp.PNG","rb") as f:
                    content = f.read()
                    allure.attach(content,name=validate["action"],attachment_type=allure.attachment_type.PNG)
                if actual_text == action.split("|")[-1]:
                    result = True
                else:
                    result = False
                    self.Log.info(f"!!!!!!!{actual_text}")
        return result

'''
    def run_verify(self,validate):
        self.Log.info(f"Start Verify yaml:{validate}")
        if "by" in validate.keys():
            element = self.base_find_element(validate["by"], validate["locator"])
            if "action" in validate.keys():
                action = validate["action"]
                if action == "text":
                    actual_text=element.get_attribute('textContent')
                    if "verify" in validate.keys():
                        verify = validate["verify"]
                        verify_word = verify.split("|")[0]
                        verify_data = verify.split("|")[1]
                        if verify_word == "equal":
                            if verify_data == actual_text:
                                self.Log.info(f"A:Success:actual exist = verify,actual:{actual_text},expect:{verify_data}")
                                return True
                            else:
                                self.Log.error(f"A:Fail:actual ！= verify,actual:{actual_text},expect:{verify_data}")
                                return False
                        elif verify_word == "tbd":
                            pass
                        else:
                            pass
                elif action == "tbd":
                    pass
                else:
                    pass


    def steps(self,file_path,*krgs):
        steps = PraseYaml.get_yaml_data(file_path,*krgs)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.base_find_element(step["by"],step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()
                if action == "sendkeys":
                    element.send_keys(step["action"]["sendkeys"])
'''
if __name__ == '__main__':
    AAA=Base()
