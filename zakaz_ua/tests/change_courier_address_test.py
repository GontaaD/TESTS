import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.address
class TestMain(BaseTest):
    @allure.step("change adding products to list test start")
    def test_start(self):
        pages = PageMeneger(self.page)

        pages.address_page.set_courier_address()

        pages.check_page.add_courier_address_check()