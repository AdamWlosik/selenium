import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class SerachResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"
        self.hotel_prices_xpath = "//div[contains(@class, 'price_tab')]//b"

    @allure.step("Checking results")
    def get_hotel_names(self):
        hotels = self.driver.find_elements(By.XPATH, self.hotel_names_xpath)
        names = [hotel.get_attribute("textContent") for hotel in hotels]
        self.logger.info("Available hotels are: ")
        allure.attach(self.driver.get_screenshot_as_png(), name="results", attachment_type=AttachmentType.PNG)
        for name in names:
            self.logger.info(name)
        return names


    def get_hotel_prices(self):
        prices = self.driver.find_elements(By.XPATH, self.hotel_prices_xpath)
        hotel_prices = [price.get_attribute("textContent") for price in prices]
        self.logger.info("Prices are: ")
        for price in hotel_prices:
            self.logger.info(price)
        return hotel_prices

