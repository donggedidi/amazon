import logging
import os,sys
from time import sleep

sys.path.append(os.getcwd())
from base.base_driver import BaseDriver


from page.page import Page


class TestCart:
    def setup(self):
        self.driver=BaseDriver().get_driver()
        self.page=Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        try:
            self.page.home.page_click_login_link()
            self.page.login.page_login("christinazhai0216@163.com","1234qwer")
            self.page.home.page_input_keywords("skii")
            self.page.home.page_click_search_btn()
            self.page.search_result.page_click_product()
            self.page.search_result.page_switch_handle()
            sleep(2)
            self.page.product_detail.page_click_add_to_cart()
            info=self.page.product_detail.page_get_cart_info()
            assert info=="商品已加入购物车","加入购物车失败，请检查"


        except Exception as e:
            logging.error(e)

    def test_total_price(self):
        try:
            self.page.home.page_click_login_link()
            self.page.login.page_login("christinazhai0216@163.com", "1234qwer")
            self.page.home.page_click_cart()
            self.page.cart.page_if_check_all()
            calculate_total_price=self.page.cart.page_calculate_total_price()
            total_price_display=self.page.cart.page_total_price_display()
            print(calculate_total_price,total_price_display)
            assert total_price_display==calculate_total_price,"总价不一致，请检查"
        except Exception as e:
            logging.error("error出现了：{}".format(e))

    def test_part_total_price(self):
        self.page.home.page_click_login_link()
        self.page.login.page_login("christinazhai0216@163.com", "1234qwer")
        self.page.home.page_click_cart()
        calculate_part_total_price=self.page.cart.page_calculate_part_total_price()
        total_price_display = self.page.cart.page_total_price_display()
        logging.info("比较2个总价{},{}".format(total_price_display,calculate_part_total_price))
        assert total_price_display == calculate_part_total_price,"总价不一致，请检查"







