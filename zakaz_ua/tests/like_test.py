import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.like
class TestMain(BaseTest):
    @allure.step("product like test start")
    def test_start(self):
        pages = PageMeneger(self.page)

        pages.main_page.open_bbq_category()

        pages.bbq_page.click_heart_button()

        productTitle1 = pages.bbq_page.search_product_name_in_catalog()

        pages.main_page.open_list_menu()

        productTitle2 = pages.list_page.search_product_name_in_list()

        pages.check_page.like_availability_check(productTitle1, productTitle2)

        pages.main_page.remove_like()