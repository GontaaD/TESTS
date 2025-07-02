from zakaz_ua.pages.main_page import MainPage
from zakaz_ua.pages.login_page import LoginPage
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.list_page import ListPage


class TestMain(BaseTest):
    def test_start(self):
        main_page = MainPage(self.page)
        login_page = LoginPage(self.page)
        list_page = ListPage(self.page)

        self.page.goto("https://www.zakaz.ua", wait_until="load")

        new_list_name = "лист"

        login_page.login()

        main_page.open_list_menu()

        old_list_name = list_page.save_old_list_name()

        list_page.rename_list(new_list_name)

        list_page.rename_check(new_list_name, old_list_name)