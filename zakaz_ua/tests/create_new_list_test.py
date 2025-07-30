import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.ui
@pytest.mark.list
class TestMain(BaseTest):
    @allure.step("create new list test start")
    def test_start(self):
        pages = PageMeneger(self.page)

        pages.main_page.open_list_menu()

        new_list_name = pages.list_page.generate_list_name()

        pages.list_page.create_new_list(new_list_name)

        pages.check_page.create_new_list_test(new_list_name)

        pages.list_page.delete_list(new_list_name)




