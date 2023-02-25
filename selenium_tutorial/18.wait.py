import time
from time import sleep
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
'''driver.implicitly_wait(10)''' # lepsze niż sleep bo czeka do pojawianie sie elementu  lub po 10 sek bład
                           # metoda podpinane do każdego elementy w skrypcie co wypływa na wydajnosc
wait = WebDriverWait(driver, 10, 0.5)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Waits2.html")
#driver.maximize_window()
driver.find_element(By.ID, "clickOnMe").click()
wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "p"))) #oczekowanie na widocznosc elementu p
print(driver.find_element(By.TAG_NAME, "p").text)

sleep(1)
driver.quit()