from time import sleep

from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Test.html")
driver.maximize_window()

driver.find_element(By.ID, "newPage").click()
print(driver.title)
current_window_name= driver.current_window_handle # przypisanie aktualnego okna do zmiennej
window_name = driver.window_handles # przypisujemy wszystkie okna do zmiennje

for window in window_name:
    if window != current_window_name:
        driver.switch_to.window(window) # jeżeli okno z listy innego od pierwotnego okna to przepinamy sie do okna z listy

print(driver.title)

sleep(1)
driver.quit()