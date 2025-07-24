import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.search
class TestMain(BaseTest):
    @allure.step("search special symbol field test")
    def test_start(self):
        special_symbol_name = "ʼ;пиво hei;--"

        pages = PageMeneger(self.page)

        pages.main_page.search_product(special_symbol_name)

        pages.check_page.search_with_special_symbol_field_check(special_symbol_name)