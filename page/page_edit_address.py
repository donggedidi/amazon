import logging

import page
from base.base_action import BaseAction


class PageEditAddress(BaseAction):
    def page_input_address(self,address):
        logging.info("输入地址{}".format(address))
        self.base_input(page.address_info,address)

    def page_select_area(self):

        self.base_select_drop_down(page.provinces,1)
        self.base_select_drop_down(page.city, 1)
        self.base_select_drop_down(page.district, 1)

    def page_save_address_btn(self):
        self.base_click(page.save_btn)

    def page_save_result(self):
        return self.base_get_text(page.save_info)




