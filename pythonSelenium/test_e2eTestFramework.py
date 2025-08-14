from selenium.webdriver.common.by import By

def test_e2e(browser_instance):
    user_email = "a@a.com"
    user_password = "123"
    driver = browser_instance
    driver.get("http://ec2-54-177-188-240.us-west-1.compute.amazonaws.com/")
    driver.find_element(By.LINK_TEXT, "Sign in").click()
    driver.find_element(By.ID, "email").send_keys(user_email)
    driver.find_element(By.ID, "password").send_keys(user_password)
    driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
    email_text = driver.find_element(By.XPATH, "//p[contains(text(), '@')]").text
    email = email_text.split("|")[0].strip()
    assert user_email == email




