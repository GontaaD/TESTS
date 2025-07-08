import allure
from zakaz_ua.pages.base_page import BasePage

class MainPagelocators(BasePage):
    CATEGORY_BUTTON = "//button[@class='CategoriesMenuButton__inner']"
    BBQ_CATEGORY_BUTTON = "//a[contains(@href, '/bbq-season-zakaz/')]"
    ACCOUNT_NAVIGATOR = "//div[@data-marker='account navigation']"
    LIST_MENU = "//*[text()='Списки']//ancestor::p[@data-sentry-element='StyledComponent']"
    LIKE_BUTTON = "//button[@data-marker='Favorite button']"

    def __init__(self, page):
        self.page = page

class MainPage(BasePage):
    @allure.step("click category button")
    def click_category_button(self):
        self.page.click(MainPagelocators.CATEGORY_BUTTON)

    @allure.step("click bbq category button")
    def click_bbq_button(self):
        self.page.click(MainPagelocators.BBQ_CATEGORY_BUTTON)

    @allure.step("open bbq category")
    def open_bbq_category(self):
        self.click_category_button()
        self.click_bbq_button()

    @allure.step("open account navigator")
    def open_account_navigator(self):
        self.page.hover(MainPagelocators.ACCOUNT_NAVIGATOR)

    @allure.step("click list menu")
    def click_to_list_menu(self):
        self.page.click(MainPagelocators.LIST_MENU)

    @allure.step("open list menu")
    def open_list_menu(self):
        self.open_account_navigator()
        self.page.wait_for_timeout(500)
        self.click_to_list_menu()

    @allure.step("remove like")
    def remove_like(self):
        self.page.click(MainPagelocators.LIKE_BUTTON)