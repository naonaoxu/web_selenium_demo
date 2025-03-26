#encoding=utf-8
from base.base_ import Base

class Login(Base):

    def goto_frame(self):
        self.steps("../page/login.yaml")

    def email(self,email):
        self._params['email'] = email
        self.steps("../page/login.yaml")

    def password(self,password):
        self._params['password'] = password
        self.steps("../page/login.yaml")

    def login_element(self):
        self.steps("../page/login.yaml")

    def verify_click_login(self):
        pass