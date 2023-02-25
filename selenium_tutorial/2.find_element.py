from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Test.html")
driver.maximize_window()
driver.find_element(By.ID, "clickOnMe")
driver.find_element(By.NAME, "fname")
driver.find_element(By.LINK_TEXT, "Visit W3Schools.com!")
driver.find_element(By.PARTIAL_LINK_TEXT, "Visit W3")
driver.find_element(By.CLASS_NAME, "topSecret")
driver.find_element(By.TAG_NAME, "a")
driver.find_element(By.TAG_NAME, "p")
driver.find_element(By.TAG_NAME, "label")
driver.find_element(By.CSS_SELECTOR, "a")
driver.find_element(By.CSS_SELECTOR, "img#smileImage")
driver.find_element(By.CSS_SELECTOR, "p.topSecret")
print(driver.find_element(By.CSS_SELECTOR, "th:first-child").text)
driver.find_element(By.XPATH, "/html/body/table/tbody/tr/th")
driver.find_element(By.XPATH, "//tbody//th")
driver.find_element(By.XPATH, "//th")
driver.find_element(By.XPATH, "//th[text()='Month']")
driver.find_element(By.XPATH, "//button[@id='clickOnMe']")
driver.find_element(By.XPATH, "//input[@id='fname']/following-sibling::table")
driver.find_element(By.XPATH, "//input[@name='fname']/following-sibling::table")

elements_list_lenght = len(driver.find_elements(By.XPATH, "//th")) # elements
print(elements_list_lenght)


sleep(1)
driver.quit()


