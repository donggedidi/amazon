import logging

import allure

import page
from base.base_action import BaseAction


class PageSearchResult(BaseAction):
    @allure.step("点击搜索结果的第一个商品")
    def page_click_product(self):
        self.base_click_random_item(page.product_list)
        logging.info("点击商品完成")

    @allure.step("切换handle")
    def page_switch_handle(self):
        logging.info("切换之前title是:{}".format(self.driver.title))
        self.base_switch_to_handle()
        logging.info("切换之后title是:{}".format(self.driver.title))




