import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

class TestMain(BaseTest):
    @allure.step("change adding products to list test start")
    def test_start(self):
        pages = PageMeneger(self.page)

        pages.login_page.login()

        pages.address_page.select_address()

        pages.check_page.add_address_check()