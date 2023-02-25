import random
import pytest

from pages.billing_address_page import BillingAddressPage


@pytest.mark.usefixtures("setup")
class TestBillingAddress:

    def test_address_billing(self):
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_page("http://seleniumdemo.com/")
        email = str(random.randint(0, 10000)) + "adamtester@gmail.com"
        billing_address_page.register_account(email, "adamtester@")
        billing_address_page.open_billing_address_page()
        billing_address_page.billing_address_edit("Adam", "Adan", "Poland", "Gdzieś 21a", "41-250", "Bielsko",
                                                  "129938109")
        billing_address_page.save_address()

        msg = "Address changed successfully."
        assert msg in billing_address_page.is_assert_display()
