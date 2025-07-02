from zakaz_ua.pages.main_page import MainPage
from zakaz_ua.pages.BBQ_category_page import BBQPage
from zakaz_ua.pages.heart_list_page import HeartListPage
from zakaz_ua.pages.login_page import LoginPage
from zakaz_ua.tests.base_test import BaseTest


class TestMain(BaseTest):
    def test_start(self):
        main_page = MainPage(self.page)
        bbq_page = BBQPage(self.page)
        heart_list_page = HeartListPage(self.page)
        login_page = LoginPage(self.page)

        self.page.goto("https://www.zakaz.ua", wait_until="load")

        main_page.click_login_button()

        login_page.fill_number()
        login_page.fill_password()
        login_page.click_confirm_button()

        main_page.click_category_button()
        main_page.click_bbq_button()

        productTitle = bbq_page.first_search_product_name()
        bbq_page.click_heart_button()
        bbq_page.open_navigator()
        bbq_page.click_heart_list_button()

        heart_list_page.second_search_product_name()

        assert productTitle in heart_list_page.second_search_product_name()
