#encoding=utf-8
import pytest
from base.browser import Browser
from utils.prase_yaml import PraseYaml

class Test_login:

    @pytest.fixture(scope="function",autouse=True)
    def setup(self,getBrowser,getUrl):
        self.browser = Browser()
        self.main = self.browser.start(browser=getBrowser, base_url=getUrl)
        yield
        self.browser.quit_driver()

    @pytest.mark.parametrize('senario,data,validate',PraseYaml.get_yaml_data("../test_data/test_001Login.yaml", 'case1'),
                ids=[case[0] for case in PraseYaml.get_yaml_data("../test_data/test_001Login.yaml", 'case1')])
    def test_login(self, senario, data, validate):
        '''Test Login Function'''
        self.browser.Log.info(f"***Start test Senario:{senario}")
        email= data['data']['email']
        password= data['data']['password']
        verify = validate['validate']
        self.main.login().goto_frame()
        self.main.login().email(email)
        self.main.login().password(password)
        self.main.login().login_element()
        self.main.login().excute_scrollTop()
        pytest.assume(self.main.login().verify_steps(verify),f"Verify Fail:{verify}")