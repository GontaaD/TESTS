from allure import step
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.locators.BaseElement import BaseElement
from page_wrapper import PageWrapper as Pgw

class CategoryButton(BaseElement):
    @property
    def locator(self):
        return "//button[@class='CategoriesMenuButton__inner']"

class BbqCategoryButton(BaseElement):
    @property
    def locator(self):
        return "//a[contains(@href, '/bbq-season-zakaz/')]"

class EggAndMilkCategoryButton(BaseElement):
    @property
    def locator(self):
        return "//a[contains(@href, '/dairy-and-eggs-zakaz/')]"

class AccountMenu(BaseElement):
    @property
    def locator(self):
        return "//div[@data-marker='account navigation']"

class ListMenu(BaseElement):
    @property
    def locator(self):
        return "//*[text()='Списки']//ancestor::p[@data-sentry-element='StyledComponent']"

class FavoriteList(BaseElement):
    @property
    def locator(self):
        return "//*[text()='Обрані']//ancestor::p[@data-sentry-element='StyledComponent']"

class SettingsMenu(BaseElement):
    @property
    def locator(self):
        return "//*[text()='Налаштування']//ancestor::p[@data-sentry-element='StyledComponent']"

class LikeButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Favorite button']"

class SearchInput(BaseElement):
    @property
    def locator(self):
        return "//input[@data-sentry-element='SearchInput']"

class SearchResultsProduct(BaseElement):
    @property
    def locator(self):
        return "//div[@data-marker='Product Card']"

class MainPageBox(BaseElement):
    @property
    def locator(self):
        return "//main[@data-sentry-component='StylishBox']"

class VacanciesPageOpen(BaseElement):
    @property
    def locator(self):
        return "//a[contains(@href, 'https://careers.zakaz.ua/vacancies')]"

class IncorrectProductNameMessage(BaseElement):
    @property
    def locator(self):
        return "//*[text()='Ми не змогли знайти результати для']//ancestor::p[@data-sentry-element='StyledComponent']"

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wrapper = Pgw(page)
        self.category_button = CategoryButton(self.page)
        self.bbq_category_button = BbqCategoryButton(self.page)
        self.account_menu = AccountMenu(self.page)
        self.list_menu = ListMenu(self.page)
        self.like_button = LikeButton(self.page)
        self.search_input = SearchInput(self.page)
        self.search_results_product = SearchResultsProduct(self.page)
        self.main_page_box = MainPageBox(self.page)
        self.settings_menu = SettingsMenu(self.page)
        self.vacancies_page_open = VacanciesPageOpen(self.page)
        self.incorrect_product_name_message = IncorrectProductNameMessage(self.page)
        self.eggs_and_milk_category_button = EggAndMilkCategoryButton(self.page)
        self.favorite_list = FavoriteList(self.page)

    @step("open bbq category")
    def open_bbq_category(self):
        self.category_button.click()
        self.bbq_category_button.click()

    @step("open egg and milk category")
    def open_egg_and_milk_category(self):
        self.category_button.click()
        self.eggs_and_milk_category_button.click()

    @step("open list menu")
    def open_list_menu(self):
        self.account_menu.click()
        self.list_menu.wait_for(state="visible").click()
        self.favorite_list.wait_for(state="visible", timeout=5000)

    @step("remove like")
    def remove_like(self):
        if self.like_button.is_visible():
            self.like_button.click()

    @step("scroll and input product name")
    def search_product(self, search_name):
        self.main_page_box.click()
        self.search_input.scroll_into_view_if_needed()
        self.search_input.wait_for(state="visible").type(search_name, 100)

    @step("open account settings")
    def open_account_settings(self):
        self.account_menu.click()
        self.settings_menu.wait_for(state="visible").click()

    @step("vacancies page click")
    def vacancies_page_click(self):
        self.vacancies_page_open.click()