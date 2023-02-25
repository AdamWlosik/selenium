import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome


@pytest.fixture()
def test_setup():
    global driver
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = Chrome(options=opts)
    driver.get("file:///C:/Users/adamw/OneDrive/Pulpit/selenium/Test.html")
    driver.maximize_window()
    yield
    driver.quit()


def test_method(test_setup):
    assert driver.title == "Strona testowa"


def test_method2(test_setup):
    assert driver.title == "Strona testowa"
