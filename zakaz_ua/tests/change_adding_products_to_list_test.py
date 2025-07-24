import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.list
class TestMain(BaseTest):
    @allure.step("change adding products to list test start")
    def test_start(self):
        first_list_name = "Обрані"
        second_list_name = "лист123"

        pages = PageMeneger(self.page)

        pages.main_page.open_bbq_category()

        pages.bbq_page.click_heart_button()

        productTitle1 = pages.bbq_page.search_product_name_in_catalog()

        pages.list_page.change_list(first_list_name, second_list_name)

        pages.list_page.open_another_list(second_list_name)

        productTitle2 = pages.list_page.search_product_name_in_list()

        pages.check_page.like_availability_check(productTitle1, productTitle2)

        pages.main_page.remove_like()