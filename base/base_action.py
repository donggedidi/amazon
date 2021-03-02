import logging
import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import BaseDriver


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, time=30, poll=0.5):
        logging.info("正在查找{}".format(loc))
        return WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_find_elements(self, loc, time=30, poll=0.5):
        logging.info("正在查找列表{}".format(loc))
        return WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    def base_click(self, loc):
        logging.info("正在点击{}".format(loc))
        self.base_find_element(loc).click()
        logging.info("点击{}完成".format(loc))

    def base_input(self, loc, value):
        logging.info("正在查找{}".format(loc))
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    def base_get_text(self, loc):
        logging.info("正在获取{}的文本".format(loc))
        return self.base_find_element(loc).text

    def base_get_screenshot(self):
        logging.info("正在截图")
        self.driver.get_screenshot_as_file("../screenshot/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
        logging.info("完成截图")

    def base_if_exist(self, feature):
        try:
            if self.base_find_element(feature, time=10):
                logging.info("正在查找是否存在{}".format(feature))
                return True
        except Exception as e:
            return False

    def base_back_to_index(self, url):
        logging.info("正在返回页面{}".format(url))
        self.driver.get(url)
        logging.info("成功返回{}".format(url))

    def base_switch_to_iframe(self, frame):
        logging.info("正在切换到frame{}".format(frame))
        self.driver.switch_to.frame(frame)
        logging.info("成功切换frame")

    def base_switch_to_default(self):
        logging.info("正在返回默认页面")
        self.driver.switch_to.default_content()
        logging.info("成功返回默认页面")

    def base_switch_to_handle(self):
        handles = self.driver.window_handles
        current_handle=self.driver.current_window_handle
        for handle in handles:
            if handle!=current_handle:
                self.driver.switch_to.window(handle)
                logging.info("完成切换handle")

    def base_click_random_item(self, feature):
        logging.info("正在点击任意一个item")
        item_list = self.base_find_elements(feature)
        item_count = len(item_list)
        item_index = random.randint(0, item_count - 1)
        # logging.info("选取任意索引：{}".format(item_index))
        # item_list[item_index].click()
        ActionChains(self.driver).move_to_element(item_list[item_index]).click(item_list[item_index]).perform()
        logging.info("任意一个item已经点击完成")



    def base_mouse_over(self,feature):
        element=self.base_find_element(feature)
        action=ActionChains(self.driver)
        action.move_to_element(element).perform()

    def base_select_drop_down(self,feature,index):
        element=self.base_find_element(feature)
        select=Select(element)
        select.select_by_index(index)

    def base_split_price(self,text):
        str = ""
        arr = text[1:].split(",")
        return float(str.join(arr))

    # def base_caculate_total_price(self,price_feature,quantity_feature):
    #     price_list=self.base_find_elements(price_feature)
    #     quantity_list=self.base_find_elements(quantity_feature)
    #     calculate_total_price=0
    #     for i in range(0,len(price_list)):
    #         price_str=price_list[i].text
    #         actual_price=self.base_split_price_list(price_str)
    #         product_quantity_int = int(quantity_list[i].text)
    #         result=actual_price*product_quantity_int
    #         calculate_total_price +=result
    #     return calculate_total_price

    def base_caculate_one_product_price(self,price_list,quantity_list,i):
        price_str = price_list[i].text
        actual_price = self.base_split_price(price_str)
        product_quantity_int = int(quantity_list[i].text)
        result = actual_price * product_quantity_int
        return result


if __name__ == '__main__':
    driver = BaseDriver().get_driver()
    BaseAction(driver).base_click((By.ID, "haha"))
