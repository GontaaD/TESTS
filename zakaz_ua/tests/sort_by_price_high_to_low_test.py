import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.ui
@pytest.mark.filter
class TestMain(BaseTest):
    @allure.step("vacancies filter test start")
    def test_start(self):
        pages = PageMeneger(self.page)

        pages.main_page.open_bbq_category()

        pages.bbq_page.set_high_sort_price()

        pages.check_page.sort_by_price_high_check()