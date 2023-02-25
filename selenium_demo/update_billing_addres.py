from selenium.webdriver import ChromeOptions, Chrome, Keys
from selenium.webdriver.common.by import By
import random

from selenium.webdriver.support.select import Select


def test_update_billing_address():
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = Chrome(options=options)
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/")

    email = str(random.randint(0, 10000)) + "adamtester@gmail.com"
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("adamtester@")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    driver.find_element(By.LINK_TEXT, "Addresses").click()
    driver.find_element(By.LINK_TEXT, "Edit").click()
    driver.find_element(By.ID, "billing_first_name").send_keys("Adam")
    driver.find_element(By.ID, "billing_last_name").send_keys("Adam")
    Select(driver.find_element(By.ID, "billing_country")).select_by_visible_text("Poland")
    driver.find_element(By.ID, "billing_address_1").send_keys("Gdzies ta 21")
    driver.find_element(By.ID, "billing_postcode").send_keys("41-250")
    driver.find_element(By.ID, "billing_city").send_keys("Bielsko")
    driver.find_element(By.ID, "billing_phone").send_keys("129938109")
    driver.find_element(By.XPATH, "//button[@value='Save address']").click()

    assert "Address changed successfully." in driver.find_element(By.XPATH, "//div[@class='woocommerce-message']").text
