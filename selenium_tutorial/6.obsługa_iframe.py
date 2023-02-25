from time import sleep

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/iFrameTest.html")
driver.maximize_window()

print(driver.find_element(By.TAG_NAME, "h1").text)
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
print(driver.find_element(By.TAG_NAME, "h1").text)
driver.switch_to.default_content() # powrt do domystorny

sleep(1)
driver.quit()