from zakaz_ua.pages.main_page import MainPage
from zakaz_ua.pages.BBQ_category_page import BBQPage
from zakaz_ua.pages.login_page import LoginPage
from zakaz_ua.tests.base_test import BaseTest


class TestMain(BaseTest):
    def test_start(self):
        main_page = MainPage(self.page)
        bbq_page = BBQPage(self.page)
        login_page = LoginPage(self.page)

        self.page.goto("https://www.zakaz.ua", wait_until="load")

        main_page.click_login_button()

        login_page.login()

        main_page.open_category()

        min_price = 80
        max_price = 300

        bbq_page.fill_price_filter(min_price, max_price)
        bbq_page.check_all_prices_in_range(min_price, max_price)

