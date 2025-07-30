import pytest
import allure
from zakaz_ua.tests.base_test import BaseTest
from zakaz_ua.pages.Page_manager import PageMeneger

@pytest.mark.ui
@pytest.mark.filter
class TestMain(BaseTest):
    @allure.step("vacancies filter test start")
    def test_start(self):
        pages = PageMeneger(self.page)

        city_name = "Рівне"

        directions = "Дистанційна робота"

        pages.check_page.filter_without_vacancies_check(city_name, directions)

