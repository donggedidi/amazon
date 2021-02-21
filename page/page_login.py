from time import sleep

import allure

import page
from base.base_action import BaseAction


class PageLogin(BaseAction):
    @allure.step("输入邮箱")
    def page_input_email(self,email):
        allure.attach("输入邮箱：{}".format(email))
        self.base_input(page.email,email)

    @allure.step("点击继续按钮")
    def page_click_continue_btn(self):
        self.base_click(page.continue_btn)

    @allure.step("输入密码")
    def page_input_password(self,password):
        allure.attach("输入密码：{}".format(password))
        self.base_input(page.password,password)

    @allure.step("点击登录按钮")
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    @allure.step("获取页面上的错误提示")
    def page_get_error_text(self):
        error_list=self.base_find_elements(page.error)
        for i in error_list:
            # print("text:{}".format(i.text))
            # print(type(i))
            if len(i.text) != 0:
                # print("if text:{}".format(i.text))
                # print(type(i.text))
                return i.text




    def page_login(self,email,password):
        try:
            self.page_input_email(email)
            self.page_click_continue_btn()
            self.page_input_password(password)
            sleep(3)
            self.page_click_login_btn()
        except:
            raise Exception

