from selenium.webdriver.common.by import By

from pythonSelenium.pageObjects.LoginPage import LoginPage
from pythonSelenium.pageObjects.ShopPage import ShopPage


def test_e2e(browser_instance):
    driver = browser_instance
    driver = browser_instance
    driver.get("http://ec2-54-177-188-240.us-west-1.compute.amazonaws.com/")



    # user_email = "a@a.com"
    # login_page = LoginPage(driver)
    # login_page.login()
    # email_text = driver.find_element(By.XPATH, "//p[contains(text(), '@')]").text
    # email = email_text.split("|")[0].strip()
    # assert user_email == email
    add_deal_items = ShopPage(driver)
    add_deal_items.add_product_to_cart()






