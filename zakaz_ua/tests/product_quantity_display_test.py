import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.search
class TestMain(BaseTest):
    @allure.step("vacancies filter test start")
    def test_start(self):
        pages = PageMeneger(self.page)

        pages.main_page.open_bbq_category()

        pages.check_page.product_quantity_display_check()