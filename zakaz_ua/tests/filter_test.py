from zakaz_ua.pages.main_page import MainPage
from zakaz_ua.pages.BBQ_category_page import BBQPage
from zakaz_ua.pages.login_page import LoginPage
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.CheckTest_page import CheckTestPage


class TestMain(BaseTest):
    def test_start(self):
        main_page = MainPage(self.page)
        bbq_page = BBQPage(self.page)
        login_page = LoginPage(self.page)
        check_page = CheckTestPage(self.page)

        self.page.goto("https://www.zakaz.ua", wait_until="load")

        login_page.login()

        main_page.open_bbq_category()

        enter_min_price = 80
        enter_max_price = 300

        bbq_page.fill_price_filter(enter_min_price, enter_max_price)
        check_page.check_all_prices_in_range(enter_min_price, enter_max_price)