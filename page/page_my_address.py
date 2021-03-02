import allure

import page
from base.base_action import BaseAction


class PageMyAddress(BaseAction):
    @allure.step("判断地址是否存在")
    def page_if_address(self):
        return self.base_if_exist(page.address_list)

    def page_click_new_address_btn(self):
        self.base_click(page.new_address_btn)


