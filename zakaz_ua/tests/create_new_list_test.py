from zakaz_ua.pages.main_page import MainPage
from zakaz_ua.pages.login_page import LoginPage
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.list_page import ListPage
from zakaz_ua.pages.CheckTest_page import CheckTestPage

class TestMain(BaseTest):
    name_for_new_list = "новий лист"

    def test_start(self, name_for_new_list):
        main_page = MainPage(self.page)
        login_page = LoginPage(self.page)
        list_page = ListPage(self.page)
        check_page = CheckTestPage(self.page)

        self.page.goto("https://www.zakaz.ua", wait_until="load")



        login_page.login()

        main_page.open_list_menu()

        list_page.create_new_list(name_for_new_list)

        check_page.create_new_list_test()




