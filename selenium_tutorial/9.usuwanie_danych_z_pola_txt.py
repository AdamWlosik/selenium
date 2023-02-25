from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Test.html")
driver.maximize_window()

username_input = driver.find_element(By.NAME, "username")
username_input.clear() # czyszczenie txt
username_input.send_keys("JakasWartosc")

#sleep(1)
#driver.quit()