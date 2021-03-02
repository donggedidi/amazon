import allure

import page
from base.base_action import BaseAction


class PageProductDetail(BaseAction):
    @allure.step("加入购物车")
    def page_click_add_to_cart(self):
        self.base_click(page.add_to_cart)

    @allure.step("获取加入购物车结果文本")
    def page_get_cart_info(self):
        return self.base_get_text(page.add_to_cart_info)

