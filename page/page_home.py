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

    @allure.step("输入框输入内容")
    def page_input_keywords(self,keywords):
        allure.attach("搜索关键字是：{}".format(keywords))
        self.base_input(page.search_box,keywords)

    @allure.step("点击搜索按钮")
    def page_click_search_btn(self):
        self.base_click(page.search_btn)


    # @allure.step("mouse over在我的账户上")
    # def page_mouse_over_my_account(self):
    #     self.base_mouse_over(page.my_account)

    @allure.step("点击在我的账户上")
    def page_click_my_account(self):
        self.base_click(page.my_account)

    def page_click_cart(self):
        self.base_click(page.cart_link)









