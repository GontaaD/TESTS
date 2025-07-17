import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.search
class TestMain(BaseTest):
    @allure.step("search_part_field_test_start")
    def test_start(self):
        incorrect_product_name = "wkhfljyr"

        pages = PageMeneger(self.page)

        pages.login_page.login()

        pages.main_page.search_product(incorrect_product_name)

        pages.check_page.incorrect_product_name_search_check()