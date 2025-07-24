import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.settings
class TestMain(BaseTest):
    @allure.step("search field test start")
    def test_start(self):
        pages = PageMeneger(self.page)

        invalid_email = "gontadenis@com"

        pages.main_page.open_account_settings()

        pages.settings_page.input_email_invalid_format(invalid_email)

        pages.check_page.add_email_invalid_format_check()

        pages.settings_page.return_old_email()