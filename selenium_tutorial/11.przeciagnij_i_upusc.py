from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome


opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")
driver.maximize_window()
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

draggable = driver.find_element(By.ID, "draggable")
drop_target = driver.find_element(By.ID, "droptarget")

webdriver.ActionChains(driver).drag_and_drop(draggable,drop_target).perform()

#sleep(1)
#driver.quit()