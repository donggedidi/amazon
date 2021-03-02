import allure

import page
from base.base_action import BaseAction


class PageMyAccount(BaseAction):
    @allure.step("点击新增地址")
    def page_new_address(self):
        self.base_click(page.address_link)



