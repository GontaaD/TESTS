import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

class TestMain(BaseTest):
    @allure.step("product like test start")
    def test_start(self):
        pages = PageMeneger(self.page)

        pages.login_page.login()

        pages.main_page.open_bbq_category()

        pages.bbq_page.click_heart_button()

        pages.main_page.open_list_menu()

        pages.check_page.like_availability_check()

        pages.main_page.remove_like()