from selenium.webdriver.common.by import By

URL="https://www.amazon.cn/"
"""homepage"""
login_link=By.ID,"nav-link-yourAccount"
account_name=By.ID,"nav-link-yourAccount"
logo=By.CSS_SELECTOR,".nav-logo-base"
search_box=By.ID,"twotabsearchtextbox"
search_btn=By.CSS_SELECTOR,".nav-input"
my_account=By.CSS_SELECTOR,".nav-a.nav-a-2.nav-truncate"
cart_link=By.ID,"nav-cart"


"""login_page"""
email=By.ID,"ap_email"
continue_btn=By.ID,"continue"
password=By.ID,"ap_password"
login_btn=By.ID,"signInSubmit"
error=By.CSS_SELECTOR,".a-alert-content"

"""search_result"""
goods_list=By.CSS_SELECTOR,".a-section.aok-relative"

"""goods_detail"""
add_to_cart=By.CSS_SELECTOR,"#add-to-cart-button"
add_to_cart_info=By.CSS_SELECTOR,".a-size-medium.a-text-bold"

"""edit_address"""
address_info=By.CSS_SELECTOR,"#address-ui-widgets-enterAddressLine1"
provinces=By.NAME,"address-ui-widgets-enterAddressStateOrRegion"
city=By.NAME,"address-ui-widgets-enterAddressCity"
district=By.NAME,"address-ui-widgets-enterAddressDistrictOrCounty"
save_btn=By.CSS_SELECTOR,".a-button-input"
save_info=By.CSS_SELECTOR,".a-alert-heading"

"""my_account"""
address_link=By.XPATH,"(//*[@class='ya-card__whole-card-link'])[4]"

"""my_address"""
new_address_btn=By.CSS_SELECTOR,".a-box.first-desktop-address-tile"
address_list=By.CSS_SELECTOR,".a-box.a-spacing-none"

"""cart"""
# product_price=By.XPATH,"//*[@class='a-row a-spacing-base a-spacing-top-base']/*[@class='a-column a-span2 a-text-right sc-item-right-col a-span-last']"
product_price=By.CSS_SELECTOR,".a-size-medium.a-color-base.sc-price.sc-white-space-nowrap.sc-product-price"
# product_title=By.CSS_SELECTOR,".a-row.a-spacing-base.a-spacing-top-base"
# prduct_quantity=By.XPATH,"//*[@class='a-row a-spacing-base a-spacing-top-base']//*[@class='a-button-text a-declarative']"
prduct_quantity=By.CSS_SELECTOR,".a-dropdown-prompt"
total_price_list=By.CSS_SELECTOR,".a-size-medium.a-color-base"
select_all=By.ID,"select-all"
deselect_all=By.ID,"deselect-all"
# check_box=By.CSS_SELECTOR,".a-icon.a-icon-checkbox"
check_box=By.XPATH,"//input[@type='checkbox']"