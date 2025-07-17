import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.filter
class TestMain(BaseTest):
    @allure.step("search field test start")
    def test_start(self):
        pages = PageMeneger(self.page)

        subcategory_name = "Сир"

        pages.login_page.login()

        pages.main_page.open_egg_and_milk_category()

        pages.egg_and_milk_category_page.open_subcategory(subcategory_name)

        pages.check_page.navigate_to_subcategory_check(subcategory_name)

