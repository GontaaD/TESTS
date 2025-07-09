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

class AccountMenu(BaseElement):
    @property
    def locator(self):
        return "//div[@data-marker='account navigation']"

class ListMenu(BaseElement):
    @property
    def locator(self):
        return "//*[text()='Списки']//ancestor::p[@data-sentry-element='StyledComponent']"

class LikeButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Favorite button']"

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wrapper = Pgw(page)
        self.category_button = CategoryButton(self.page)
        self.bbq_category_button = BbqCategoryButton(self.page)
        self.account_menu = AccountMenu(self.page)
        self.list_menu = ListMenu(self.page)
        self.like_button = LikeButton(self.page)

    @step("open bbq category")
    def open_bbq_category(self):
        self.category_button.click()
        self.bbq_category_button.click()

    @step("open list menu")
    def open_list_menu(self):
        self.account_menu.click()
        self.wrapper.wait_for_timeout(500)
        self.list_menu.click()

    @step("remove like")
    def remove_like(self):
        self.like_button.click()