from base.base_action import BaseAction
from page.page_home import PageHome
from page.page_login import PageLogin


class Page(BaseAction):
    @property
    def login(self):
        return PageLogin(self.driver)

    @property
    def home(self):
        return PageHome(self.driver)