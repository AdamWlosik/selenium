from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.support.select import Select

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Test.html")
driver.maximize_window()
'''driver.find_element(By.ID, "clickOnMe").click()'''
                # lub
'''click_me_button = driver.find_element(By.ID, "clickOnMe")
click_me_button.click()'''
driver.find_element(By.ID, "clickOnMe").click()
driver.switch_to.alert.accept() # akceptuje wyskakujący alert/okienku
driver.find_element(By.ID, "clickOnMe").click()
driver.switch_to.alert.dismiss() # zamyka alert
driver.find_element(By.ID, "fname").send_keys("Adam") # wprowadzanie do pola tekstowego
print("Element text: " + driver.find_element(By.ID, "fname").get_attribute("value")) # pobieramy text wprowadzomy wcześniej
'''driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)''' # przyciski z klawy
auto_select = Select(driver.find_element(By.TAG_NAME, "select")) # wybór opcji z rozwujanego menu
auto_select.select_by_visible_text("Volvo")
auto_select.select_by_value("saab")
auto_select.select_by_index(0)
driver.find_element(By.XPATH, "//input[@type='checkbox']").click() # wybór z klikniecie w okienko
driver.find_element(By.XPATH, "//input[@value='male']").click()
print(driver.find_element(By.TAG_NAME, "h1").text) # pobieranie tekstu
print(driver.find_element(By.ID, "clickOnMe").text)
print(driver.find_element(By.TAG_NAME, "p").get_attribute("textContent")) # pobieranie ukrytego textu ze strony

print(driver.find_element(By.ID, "smileImage").size.get("height")) # rozmiar obrazka
print(driver.find_element(By.ID, "smileImage").get_attribute("naturalHeight")) #




sleep(1)
driver.quit()