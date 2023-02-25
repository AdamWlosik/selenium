from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome


opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("https://www.w3schools.com/")
driver.maximize_window()
driver.find_element(By.ID, "accept-choices").click()
tutorials_element = driver.find_element(By.ID, "navbtn_tutorials")
'''webdriver.ActionChains(driver).move_to_element(tutorials_element).perform()''' # najechanie na element
webdriver.ActionChains(driver).move_to_element(tutorials_element). click(tutorials_element).perform()
                                                                                # najechanie i rozwiniece elementu

#sleep(1)
#driver.quit()