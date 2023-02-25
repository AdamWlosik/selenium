from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

'''driver = webdriver.Chrome()''' # driver = webdriver.Chrome(r"ścieżka do chrmoedriver.exe") jeśli nie jest dodany -
                            # - do folderu projektu
driver = webdriver.Chrome(ChromeDriverManager().install()) # instalacja ChromeDriverManager
driver.get("http://www.google.com")
'''driver.set_window_size(100, 100)''' # ustawiamy rozmiar
driver.maximize_window()
sleep(2) # usypia auto zamykanie
driver.close()  # zamyka tylko okno wywoływane z driver.get
driver.quit() # zamyka wszystkie okna
driver.find_element(By.ID, "newPage").click() # kilkamy w przycisk znaleziony po ID

# kod startowy
'''from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome


opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("https://google.com")
driver.maximize_window()

sleep(1)
driver.quit()'''