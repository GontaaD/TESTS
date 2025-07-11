import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

class TestMain(BaseTest):
    @allure.step("change adding products to list test start")
    def test_start(self):
        first_list_name = "Обрані"
        second_list_name = "лист123"

        pages = PageMeneger(self.page)

        pages.login_page.login()

        pages.main_page.open_bbq_category()

        pages.bbq_page.click_heart_button()

        pages.list_page.change_list(first_list_name, second_list_name)

        pages.check_page.like_availability_check()

        pages.main_page.remove_like()