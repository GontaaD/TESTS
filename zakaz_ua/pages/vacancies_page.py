from allure import step
from zakaz_ua.pages.base_page import BasePage
from helper.BaseElement import BaseElement

class EnabledFilterIcon(BaseElement):
    @property
    def format_locator(self):
        return "//*[text()='{city_name}']//ancestor::div[@data-testid='chipFilter']"

class VacanciesFilter(BaseElement):
    @property
    def format_locator(self):
        return "//*[text()='{filter_name}']//ancestor::div[@data-testid='filter']//div[@data-testid='checkbox']"

class VacanciesBlock(BaseElement):
    @property
    def locator(self):
        return "//a[@data-testid='vacancyCart']"

class CityNameInVacancies(BaseElement):
    @property
    def format_locator(self):
        return "//*[text()='{city_name}']//ancestor::div[@data-testid='vacancyLabel']"

class ShowMoreButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-testid='showMore']"

class ShowMoreCityesButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-testid='Show more']"

class NoVacanciesFoundMessage(BaseElement):
    @property
    def locator(self):
        return "//*[text()='За обраними фільтрами нічого не знайдено']//ancestor::div[@class='MuiBox-root css-vf8yb0']"

class ClearAllFiltersButton(BaseElement):
    @property
    def locator(self):
        return "//div[@data-testid='clearAllFilters']"

class ActivatedFilter(BaseElement):
    @property
    def format_locator(self):
        return "//*[text()='{filter_name}']//ancestor::div[@data-testid='filter']//div[@data-status='active']"

class VacanciesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.enabled_filter_icon = EnabledFilterIcon(page)
        self.vacancies_filter = VacanciesFilter(page)
        self.city_name_in_vacancies = CityNameInVacancies(page)
        self.vacancies_block = VacanciesBlock(page)
        self.show_more_button = ShowMoreButton(page)
        self.show_more_cityes_button = ShowMoreCityesButton(page)
        self.no_vacancies_found_message = NoVacanciesFoundMessage(page)
        self.clear_all_filters_button = ClearAllFiltersButton(page)
        self.activated_filter = ActivatedFilter(page)

    @step("chose city in filter")
    def city_filter_click(self, city_name):
        self.show_more_cityes_button.click()
        self.vacancies_filter.format(filter_name=city_name).click()

    @step("chose directions in filter")
    def directions_filter_click(self, directions):
        self.vacancies_filter.format(filter_name=directions).click()