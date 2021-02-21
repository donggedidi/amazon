import allure

import page
from base.base_action import BaseAction


class PageHome(BaseAction):
    @allure.step("点击登录链接")
    def page_click_login_link(self):
        self.base_click(page.login_link)

    @allure.step("获取登录用户名")
    def page_get_account_name(self):
        name=self.base_get_text(page.account_name)
        allure.attach("用户名{}".format(name))
        print("获取到的account_name:({})".format(name[4:-5]))
        return name[4:-5]

    @allure.step("回到首页")
    def page_back_to_index(self):
        self.base_click(page.logo)



