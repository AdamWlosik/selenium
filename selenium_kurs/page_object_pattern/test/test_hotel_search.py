import pytest
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SerachResultsPage
import allure

from page_object_pattern.utils.read_excel import ExcelReader


@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @allure.title("This is title")
    @allure.description("Test description")
    @pytest.mark.parametrize("data", ExcelReader.get_data())
    def test_hotel_search(self, data):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_data_range(data.check_in, data.check_out)
        search_hotel_page.set_travellers("4", "2")
        search_hotel_page.perform_search()
        results_page = SerachResultsPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        hotel_prices = results_page.get_hotel_prices()

        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"

        assert hotel_prices[0] == "$22"
        assert hotel_prices[1] == "$50"
        assert hotel_prices[2] == "$80"
        assert hotel_prices[3] == "$150"
