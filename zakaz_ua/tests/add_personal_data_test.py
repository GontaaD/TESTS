import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.ui
@pytest.mark.settings
class TestMain(BaseTest):
    @allure.step("search field test start")
    def test_start(self):
        pages = PageMeneger(self.page)

        pages.main_page.open_account_settings()

        pages.settings_page.input_personal_data()

        pages.check_page.add_personal_data_check()

        pages.main_page.open_account_settings()

        pages.settings_page.input_old_personal_data()





