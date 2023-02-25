from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome


opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Test.html")
driver.maximize_window()

first_name_input = driver.find_element(By.ID, "fname")
if first_name_input.is_enabled():
    first_name_input.send_keys("dziala")
else:
    print("element nie jest dostępny")

sleep(1)
driver.quit()