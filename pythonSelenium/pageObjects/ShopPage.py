import time

from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_deal = (By.XPATH, "//p[contains(text(),'Deals for you')]/following-sibling::div//a")

    def add_product_to_cart(self):
        total_items = len(self.driver.find_elements(*self.product_deal))

        for i in range(total_items):
            deal_links = self.driver.find_elements(*self.product_deal)
            deal_links[i].click()
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Cart')]").click()
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Continue Shopping')]").click()
            # time.sleep(3)
            if i != total_items:
                self.driver.find_element(By.XPATH, "//button[contains(text(), 'Continue Shopping')]").click()
            else:
                self.driver.find_element(By.XPATH, "//button[contains(text(), 'Checkout')]").click()

