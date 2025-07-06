from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_meneger import PageMeneger

class TestMain(BaseTest):
    def test_start(self):
        pages = PageMeneger(self.page)

        pages.login_page.login()

        pages.main_page.open_bbq_category()

        productTitle1 = pages.bbq_page.search_product_name_in_catalog()

        pages.bbq_page.click_heart_button()

        pages.main_page.open_list_menu()

        productTitle2 = pages.list_page.search_product_name_in_list()

        pages.main_page.remove_like()

        assert productTitle1 in productTitle2
