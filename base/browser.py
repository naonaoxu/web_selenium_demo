#encoding=utf-8
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from base.base_ import Base
from page.login import Login

class Browser(Base):

    def start(self, driver: WebDriver = None, browser="chrome", base_url= "https://www.baidu.com"):
        self.browser = browser
        if driver is None:
            opt = Options()
            # Trun off autoclose browser
            opt.add_experimental_option('detach', True)
            if self.browser == "chrome":
                self._driver = webdriver.Chrome(options=opt)
            elif self.browser == 'firefox':
                self.driver = webdriver.Firefox(options=opt)
            elif self.browser == 'edge':
                self.driver = webdriver.Edge(options=opt)
            else:
                self.driver = webdriver.Ie(options=opt)
            # Prevents detection of selenium use
            self._driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """
                       　　 Object.defineProperty(navigator, 'webdriver', {
                       　　 get: () => undefined})
                       　　 """})
            self.actions = ActionChains(self._driver)
            #           self.driver.implicitly_wait(3)
            self._driver.maximize_window()
        else:
            self._driver = driver

        try:
            if base_url != "":
                self.Log.info(f"***************Start open {browser},url:{base_url}")
                self._driver.get(base_url)
        except Exception as e:
            self.Log.info(f"Exception when open url {base_url}")
            raise e
        return self

    def quit_driver(self):
        if self._driver:
            self._driver.quit()
            self._driver = None
        self.Log.info(f"***************Start close webBrower")

    def login(self) -> Login:
        return Login(self._driver)



'''
    def open(self, base_url):
        try:
            if base_url != "":
                self.Log.info(f"Start open {base_url}")
                self._driver.get(base_url)
        except Exception as e:
            self.Log.info(f"Exception when open url {base_url}")
            raise e
'''

if __name__ == '__main__':
    aaa=Browser()
    aaa.start()