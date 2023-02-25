from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome


opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Test.html")
driver.maximize_window()

checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")


if checkbox.is_selected():
    print("Wartość zaznaczona, odznaczam")
    checkbox.click()
else:
    print("Zaznaczam wartość")
    checkbox.click()


sleep(1)
driver.quit()