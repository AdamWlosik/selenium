import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome


opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Waits2.html")
driver.maximize_window()

button = driver.find_element(By.ID, "clickOnMe")
button.click()
# time.sleep(5) można użuć sleep jeśli coś na stronie pojawia sie po czasie ale nie jest to najlepsze rowiazanie
print(driver.find_element(By.TAG_NAME, "p").text)

sleep(1)
driver.quit()