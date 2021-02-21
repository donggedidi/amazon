from selenium.webdriver.common.by import By

URL="https://www.amazon.cn/"
"""homepage"""
login_link=By.ID,"nav-link-yourAccount"
account_name=By.ID,"nav-link-yourAccount"
logo=By.CSS_SELECTOR,".nav-logo-base"

"""login_page"""
email=By.ID,"ap_email"
continue_btn=By.ID,"continue"
password=By.ID,"ap_password"
login_btn=By.ID,"signInSubmit"
error=By.CSS_SELECTOR,".a-alert-content"
