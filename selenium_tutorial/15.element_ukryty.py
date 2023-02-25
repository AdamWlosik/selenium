from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome


opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Test.html")
driver.maximize_window()

paragraph = driver.find_element(By.TAG_NAME, "p")
if paragraph.is_displayed():
    print("Is displayed")
    print(paragraph.text)
else:
    print("Is not displayed")
    print(paragraph.get_attribute("textContent"))

sleep(1)
driver.quit()