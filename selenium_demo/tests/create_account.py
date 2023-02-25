import random
import pytest

from pages.my_accoutn_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("adamtester@gmail.com", "adamtester@")

        msg = "Error: An account is already registered with your email address. Please log in."
        assert msg in my_account_page.get_error_msg()

    def test_create_account_passed(self):
        email = str(random.randint(0, 10000)) + "adamtester@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "adamtester@")

        assert my_account_page.is_logout_link_displayed()
