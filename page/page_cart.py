import logging
from time import sleep

import allure

import page
from base.base_action import BaseAction


class PageCart(BaseAction):
    @allure.step("计算总价")
    def page_calculate_total_price(self):
        price_list = self.base_find_elements(page.product_price)
        product_quantity=self.base_find_elements(page.prduct_quantity)
        calculate_total_price=0
        for i in range(0,len(price_list)):
            logging.info("第{}个商品".format(i))
            result=self.base_caculate_one_product_price(price_list,product_quantity,i)
            calculate_total_price +=result
        logging.info("计算总价完成")
        return calculate_total_price

    @allure.step("获取页面上的总价")
    def page_total_price_display(self):
        price_list=self.base_find_elements(page.total_price_list)
        price_amount=len(price_list)
        display_total_price=self.base_split_price(price_list[price_amount-1].text)
        return display_total_price

    @allure.step("判断是否选中全部商品")
    def page_if_check_all(self):
        try:
            if self.base_if_exist(page.select_all):
                self.base_click(page.select_all)
                logging.info("现在已经全部选中了")
                sleep(2)
        except Exception:
            logging.info("已经全部选中")

    @allure.step("取消选中任意一个商品，并计算部分商品总价")
    def page_calculate_part_total_price(self):
        # check_boxes = self.base_find_elements(page.check_box)
        self.page_if_check_all()
        sleep(2)
        price_list = self.base_find_elements(page.product_price)
        product_quantity = self.base_find_elements(page.prduct_quantity)
        self.base_click_random_item(page.check_box)
        calculate_part_total_price = 0
        sleep(5)
        check_boxes = self.base_find_elements(page.check_box)
        logging.info("checkbox总量{}".format(len(check_boxes)))
        for i in range(0, len(check_boxes)):
            if check_boxes[i].is_selected():
                logging.info("第{}个checkbox选中了".format(i))
                result = self.base_caculate_one_product_price(price_list, product_quantity, i)
                calculate_part_total_price += result
            else:
                logging.info("第{}个checkbox没选中".format(i))
                i += 1
        return calculate_part_total_price















