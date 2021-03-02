from base.base_action import BaseAction
from page.page_cart import PageCart
from page.page_edit_address import PageEditAddress
from page.page_goods_detail import PageProductDetail
from page.page_home import PageHome
from page.page_login import PageLogin
from page.page_my_account import PageMyAccount
from page.page_my_address import PageMyAddress
from page.page_search_result import PageSearchResult


class Page(BaseAction):
    @property
    def login(self):
        return PageLogin(self.driver)

    @property
    def home(self):
        return PageHome(self.driver)

    @property
    def product_detail(self):
        return PageProductDetail(self.driver)

    @property
    def search_result(self):
        return PageSearchResult(self.driver)

    @property
    def my_account(self):
        return PageMyAccount(self.driver)

    @property
    def my_address(self):
        return PageMyAddress(self.driver)

    @property
    def edit_address(self):
        return PageEditAddress(self.driver)

    @property
    def cart(self):
        return PageCart(self.driver)