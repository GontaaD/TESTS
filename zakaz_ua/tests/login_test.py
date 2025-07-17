import allure
import pytest
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger
from zakaz_ua.pages.CheckTest_page import login_test_data

@pytest.mark.login
class TestMain(BaseTest):
    @allure.step("login test start")
    @pytest.mark.parametrize("a, b, expected", login_test_data())
    def test_start(self, a, b, expected):
        pages = PageMeneger(self.page)

        pages.check_page.login_check(a, b, expected)

