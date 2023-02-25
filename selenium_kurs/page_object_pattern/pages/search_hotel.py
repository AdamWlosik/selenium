import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//div[@id='select2-drop']//input"
        self.location_match_xpath = "//span[text()='Dubai']"
        self.check_in_input_name = "checkin"
        self.check_out_input_name = "checkout"
        self.travellers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        self.search_button_xpath = "//button[text()=' Search']"

    @allure.step("Setting city name to '{1}'")
    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element(By.XPATH, self.search_hotel_span_xpath).click()
        self.driver.find_element(By.XPATH, self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, self.location_match_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set city", attachment_type=AttachmentType.PNG)

    @allure.step("Setting date rango from '{1}' to '{2}'")
    def set_data_range(self, check_in, check_out):
        self.logger.info("Setting {checkin} and {checkout}".format(checkin=check_in, checkout=check_out))
        self.driver.find_element(By.NAME, self.check_in_input_name).send_keys(check_in)
        self.driver.find_element(By.NAME, self.check_out_input_name).send_keys(check_out)
        allure.attach(self.driver.get_screenshot_as_png(), name="set date range", attachment_type=AttachmentType.PNG)

    @allure.step("Setting travellers - adults  '{1}' and children {2}'")
    def set_travellers(self, adults, child):
        self.logger.info("Setting adults - {adults} and child - {child}".format(adults=adults, child=child))
        self.driver.find_element(By.ID, self.travellers_input_id).click()
        self.driver.find_element(By.ID, self.adult_input_id).clear()
        self.driver.find_element(By.ID, self.adult_input_id).send_keys(adults)
        self.driver.find_element(By.ID, self.child_input_id).clear()
        self.driver.find_element(By.ID, self.child_input_id).send_keys(child)
        allure.attach(self.driver.get_screenshot_as_png(), name="set date range", attachment_type=AttachmentType.PNG)

    def perform_search(self):
        self.logger.info("Performing search")
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
