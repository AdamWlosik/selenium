from time import sleep
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome


opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Test.html")
driver.maximize_window()

# pierwszy sposób
elements = driver.find_elements(By.TAG_NAME, "input")
if len(elements) > 0:
    print("Element istnieje na stornie")
else:
    print("Brak elementu na stronie")

# drugi sposób
try:
    driver.find_element(By.TAG_NAME, "papa")
    print("Element istnieje na stornie")
except NoSuchElementException:
    print("Brak elementu na stronie")

sleep(1)
driver.quit()