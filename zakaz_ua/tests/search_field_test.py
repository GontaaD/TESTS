import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

class TestMain(BaseTest):
    @allure.step("search_field_test_start")
    def test_start(self):
        part_of_the_product_name = "пиво hei"

        pages = PageMeneger(self.page)

        pages.login_page.login()

        pages.main_page.search_product(part_of_the_product_name)

        pages.check_page.search_field_check(part_of_the_product_name)

