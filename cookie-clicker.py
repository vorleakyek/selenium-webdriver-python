from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from time import sleep

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

# Wait for page to load just in case
sleep(3)

# Handle initial popups (cookies consent does not have to be clicked, but language does)
print("Looking for language selection...")
try:
    # Select English language
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3) # more loading
except NoSuchElementException:
    print("Language selection not found")

cookie = driver.find_element(by=By.ID, value="bigCookie")

end_game = False
start_game_time = time.time()
start_time = time.time()

while end_game != True:

    while time.time() - start_time <= 5:
        cookie.click()

    points = driver.find_element(By.ID, "cookies").text.split()[0]
    points_int = int(points.replace(",", ""))

    item_upgrade_location = driver.find_elements(By.CSS_SELECTOR, "#products .product.unlocked.enabled")[-1]
    item_upgrade = driver.find_elements(By.CSS_SELECTOR, "#products .unlocked .price")[-1]
    item_price = item_upgrade.text
    item_price_int = int(item_price.replace(",", ""))

    if points_int >= item_price_int:
        item_upgrade_location.click()

    start_time = time.time()

    if time.time() - start_game_time > 10:
        # cookies_per_second = driver.find_element(By.ID, "cookiesPerSecond").text.split(":")[-1].strip()
        # print(cookies_per_second)
        end_game = True








# driver.quit()
