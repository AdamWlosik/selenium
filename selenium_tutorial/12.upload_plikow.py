from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
import os

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/FileUpload.html")
driver.maximize_window()

upload_input = driver.find_element(By.ID, "myFile")
path = os.path.abspath(r"C:\Users\adamw\OneDrive\Pulpit\selenium\uploadMe.txt")
upload_input.send_keys(path)

#sleep(1)
#driver.quit()