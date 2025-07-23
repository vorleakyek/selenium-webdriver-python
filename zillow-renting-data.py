import requests
from bs4 import BeautifulSoup
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from time import sleep

URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

price_tags = soup.find_all("span", attrs={"data-test": "property-card-price"})
prices = [price.getText().replace("+", "").split("/")[0] for price in price_tags]

address_tags = soup.find_all("address", attrs={"data-test": "property-card-addr"})
addresses = [address.getText(strip=True) for address in address_tags]
clean_address = [
    re.sub(r'^(.*?,|.*?\|)', '', addr).strip()
    for addr in addresses
]

link_tags = soup.find_all("a", attrs={"data-test": "property-card-link"})
links = [link.get("href") for link in link_tags]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

questions = [
    "What\'s the address of the property?",
    "What\'s the price per month?",
    "What\'s the link to the property?"
]
data = [clean_address, prices, links]

for i in range(len(addresses)):
    driver.get("https://forms.gle/x5BKJhTzfaWiPZst6")
    sleep(2)

    try:
        for j in range(len(questions)):
            xpath = f'//span[contains(text(), "{questions[j]}")]/ancestor::div/following::input[1]'
            answer_input = driver.find_element(By.XPATH, xpath)
            answer_input.send_keys(data[j][i])

        submit_btn = driver.find_element(By.XPATH, '//span[contains(text(), "Submit")]')
        submit_btn.click()

    except NoSuchElementException:
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("address question is not found")
