import logging
import os,sys
sys.path.append(os.getcwd())


import pytest
from time import sleep
from base.base_data import BaseData
from base.base_driver import BaseDriver
from page.page import Page

# logger = BaseLogging().get_logging()

class TestLogin:

    def setup(self):
        self.driver=BaseDriver().get_driver()
        self.page=Page(self.driver)

    def teardown(self):
        logging.info("完成测试")
        self.driver.quit()

    @pytest.mark.parametrize(("email","password","account_name","error"),BaseData().read_data("login.txt"))
    def test_login(self,email,password,account_name,error):
        logging.info("点击登录链接")
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
                assert error==self.page.login.page_get_error_text(),"断言有问题，请检查"








