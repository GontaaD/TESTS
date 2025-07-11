import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

class TestMain(BaseTest):
    @allure.step("rename test start")
    def test_start(self):
        start_list_name = "лист123"
        new_list_name = "лист"

        pages = PageMeneger(self.page)

        pages.login_page.login()

        pages.main_page.open_list_menu()

        old_list_name = pages.list_page.save_old_list_name(start_list_name)

        pages.list_page.rename_list(start_list_name, new_list_name)

        pages.check_page.rename_check(new_list_name, old_list_name)

        pages.list_page.back_old_list_name(start_list_name, new_list_name)