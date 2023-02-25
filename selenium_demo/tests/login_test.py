import pytest

from pages.my_accoutn_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("adamtester@gmail.com", "adamtester@")

        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("zle@gmail.com", "adamtester@")

        msg = "ERROR: Incorrect username or password."
        assert msg in my_account_page.get_error_msg()
