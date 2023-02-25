from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/DoubleClick.html")
driver.maximize_window()

button = driver.find_element(By.ID, "bottom")
button.click() #click lewym
'''webdriver.ActionChains(driver).double_click(button).perform()''' # 2 * click lewym
webdriver.ActionChains(driver).context_click(button).perform() # click prawym


#sleep(1)
#driver.quit()