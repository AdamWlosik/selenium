from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Test.html")
driver.maximize_window()
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "newPage"))
wartosc = "Adam"
driver.execute_script("arguments[0].setAttribute('value', '" + wartosc + "')", driver.find_element(By.ID, "fname"))

sleep(1)
driver.quit()