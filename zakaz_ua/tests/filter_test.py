import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_meneger import PageMeneger

class TestMain(BaseTest):
    @allure.step("product filter test start")
    def test_start(self):
        enter_min_price = 80
        enter_max_price = 300

        pages = PageMeneger(self.page)

        pages.login_page.login()

        pages.main_page.open_bbq_category()

        pages.bbq_page.set_price_filter(enter_min_price, enter_max_price)

        pages.check_page.check_all_prices_in_range(enter_min_price, enter_max_price)