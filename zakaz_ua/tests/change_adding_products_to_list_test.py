from zakaz_ua.pages.main_page import MainPage
from zakaz_ua.pages.BBQ_category_page import BBQPage
from zakaz_ua.pages.list_page import ListPage
from zakaz_ua.pages.login_page import LoginPage
from zakaz_ua.tests.base_test import BaseTest


class TestMain(BaseTest):
    def test_start(self):
        main_page = MainPage(self.page)
        bbq_page = BBQPage(self.page)
        list_page = ListPage(self.page)
        login_page = LoginPage(self.page)

        self.page.goto("https://www.zakaz.ua", wait_until="load")

        login_page.login()

        main_page.open_bbq_category()

        productTitle1 = bbq_page.search_product_name_in_catalog()

        bbq_page.click_heart_button()

        list_page.change_list()

        list_page.check_product_in_second_list()

        productTitle2 = list_page.search_product_name_in_list()

        main_page.remove_like()

        assert productTitle1 in productTitle2