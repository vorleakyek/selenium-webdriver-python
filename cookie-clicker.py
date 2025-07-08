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


start_time = time.time()

while time.time() - start_time <=5:
    for i in range(100):
        cookie.click()
# start_time = time.time()


points = driver.find_element(By.ID, "cookies").text.split()[0]
print(points)


