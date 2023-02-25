from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BillingAddressPage:

    def __init__(self, driver):
        self.driver = driver
        self.my_account_button_xpath = "//li[@id='menu-item-22']//a"
        self.reg_email_input_id = "reg_email"
        self.reg_password_input_id = "reg_password"
        self.addresses_link_link_text = "Addresses"
        self.edit_link_link_text = "Edit"
        self.first_name_input_id = "billing_first_name"
        self.last_name_input_id = "billing_last_name"
        self.country_select_id = "billing_country"
        self.address_input_id = "billing_address_1"
        self.postcode_input_id = "billing_postcode"
        self.city_input_id = "billing_city"
        self.phone_input_id = "billing_phone"
        self.save_address_button_xpath = "//button[@value='Save address']"
        self.message_div_xpath = "//div[@class='woocommerce-message']"

    def open_page(self, page_address):
        self.driver.get(page_address)

    def register_account(self, email, password):
        self.driver.find_element(By.XPATH, self.my_account_button_xpath).click()
        self.driver.find_element(By.ID, self.reg_email_input_id).send_keys(email)
        self.driver.find_element(By.ID, self.reg_password_input_id).send_keys(password)
        self.driver.find_element(By.ID, self.reg_password_input_id).send_keys(Keys.ENTER)

    def open_billing_address_page(self):
        self.driver.find_element(By.LINK_TEXT, self.addresses_link_link_text).click()
        self.driver.find_element(By.LINK_TEXT, self.edit_link_link_text).click()

    def billing_address_edit(self, first_name, last_name, country, address, poste_code, city, phone):
        self.driver.find_element(By.ID, self.first_name_input_id).send_keys(first_name)
        self.driver.find_element(By.ID, self.last_name_input_id).send_keys(last_name)
        Select(self.driver.find_element(By.ID, self.country_select_id)).select_by_visible_text(country)
        self.driver.find_element(By.ID, self.address_input_id).send_keys(address)
        self.driver.find_element(By.ID, self.postcode_input_id).send_keys(poste_code)
        self.driver.find_element(By.ID, self.city_input_id).send_keys(city)
        self.driver.find_element(By.ID, self.phone_input_id).send_keys(phone)

    def save_address(self):
        self.driver.find_element(By.XPATH, self.save_address_button_xpath).click()

    def is_assert_display(self):
        return self.driver.find_element(By.XPATH, self.message_div_xpath).text








