from zakaz_ua.locators.locators import MainPagelocators
from zakaz_ua.pages.base_page import BasePage

class MainPage(BasePage):
    def click_login_button(self):
        self.page.click(MainPagelocators.LOGIN_BUTTON)

    def click_category_button(self):
        self.page.click(MainPagelocators.CATEGORY_BUTTON)

    def click_bbq_button(self):
        self.page.click(MainPagelocators.BBQ_CATEGORY_BUTTON)

