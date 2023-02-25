from time import sleep

import pytest

from selenium.webdriver import ChromeOptions, Chrome


@pytest.fixture()
def setup(request):
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    sleep(1)
    driver.quit()
