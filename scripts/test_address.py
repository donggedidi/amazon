import os,sys
from time import sleep

sys.path.append(os.getcwd())
import logging

from base.base_driver import BaseDriver
from page.page import Page


class TestAddress:
    def setup(self):
        logging.info("正在获取driver对象")
        self.driver=BaseDriver().get_driver()
        self.page=Page(self.driver)

    def teardown(self):
        logging.info("关闭浏览器")
        self.driver.quit()

    def test_address(self):
        self.page.home.page_click_login_link()
        self.page.login.page_login("christinazhai0216@163.com", "1234qwer")
        self.page.home.page_click_my_account()
        self.page.my_account.page_new_address()
        if self.page.my_address.page_if_address():
            print("地址存在，不用新建了")
            logging.info("有地址")

        else:
            self.page.my_address.page_click_new_address_btn()
            sleep(1)
            self.page.edit_address.page_select_area()
            self.page.edit_address.page_input_address("test address")
            self.page.edit_address.page_save_address_btn()
            assert self.page.edit_address.page_save_result()=="已保存地址"



