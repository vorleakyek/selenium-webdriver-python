# import sys
# import os
#
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from selenium.webdriver.common.by import By

# from pythonSelenium.pageObjects.LoginPage import LoginPage
from pythonSelenium.pageObjects.ShopPage import ShopPage
# import webbrowser


def test_e2e(browser_instance):
    driver = browser_instance
    driver.get("http://ec2-54-177-188-240.us-west-1.compute.amazonaws.com/")

    # Login
    # user_email = "a@a.com"
    # login_page = LoginPage(driver)
    # login_page.login()
    # email_text = driver.find_element(By.XPATH, "//p[contains(text(), '@')]").text
    # email = email_text.split("|")[0].strip()
    # assert user_email == email

    # Add items
    add_deal_items = ShopPage(driver)
    add_deal_items.add_two_products_to_cart_with_changing_quantity()
    prices_elements = driver.find_elements(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div//span[contains(@class, 'text-rose-500')]"
    )
    prices = [float(price.text.split("$")[1]) for price in prices_elements]
    expected_total_price = sum(prices)

    order_summary = driver.find_elements(By.XPATH, "//h3[contains(text(),'Order Summary')]/following-sibling::div//p")
    display_total_price = float(order_summary[4].text.split("$")[1])
    assert expected_total_price == display_total_price 




    # webbrowser.open("report.html")

    # checkout




