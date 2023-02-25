from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.support.wait import WebDriverWait

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
wait = WebDriverWait(driver, 10, 0.5)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Waits2.html")
#driver.maximize_window()
driver.find_element(By.ID, "clickOnMe").click()
wait.until(lambda wd: len(wd.find_element(By.TAG_NAME, "p")) == 1)
print(driver.find_element(By.TAG_NAME, "p").text)

sleep(1)
driver.quit()