import os,sys
sys.path.append(os.getcwd())
from selenium.common.exceptions import TimeoutException

import page



import pytest
from time import sleep
from base.base_data import BaseData
from base.base_driver import BaseDriver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver=BaseDriver().get_driver()
        self.page=Page(self.driver)

    def teardown(self):
        BaseDriver().driver_quit()

    @pytest.mark.parametrize(("email","password","account_name","error"),BaseData().read_data("login.yaml"))
    def test_login(self,email,password,account_name,error):
        self.page.home.page_click_login_link()
        sleep(2)
        if error == None:
            self.page.login.page_login(email, password)
            display_name = self.page.home.page_get_account_name()
            assert display_name==account_name,"登录失败"
            print("{}登录成功".format(display_name))
        else:
            try:
                self.page.login.page_login(email, password)
            except Exception:
                print("数据里到error:{}".format(error))
                print("页面上获取到到error：{}".format(self.page.login.page_get_error_text()))
                assert error==self.page.login.page_get_error_text(),"断言有问题，请检查"



        # self.page.login.page_input_email(email)
        # self.page.login.page_click_continue_btn()
        # sleep(3)
        # print(self.page.login.page_get_error_text())







