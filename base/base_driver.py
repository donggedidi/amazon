from selenium import webdriver

import page
class BaseDriver:
    driver=None
    def get_driver(self):
        if self.driver is None:
            self.driver=webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(page.URL)
            return self.driver

    def driver_quit(self):
        if self.driver:
            self.driver.quit()
            self.driver=None

if __name__ == '__main__':
    BaseDriver().get_driver()


