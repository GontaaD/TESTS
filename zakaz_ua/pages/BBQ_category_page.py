from zakaz_ua.locators.locators import BBQCategoryPageLocators
from zakaz_ua.pages.base_page import BasePage

class BBQPage(BasePage):
    def click_heart_button(self):
        self.page.click(BBQCategoryPageLocators.HEART_BUTTON)

    def first_search_product_name(self):
        return self.get_text(BBQCategoryPageLocators.PRODUCT_TITLE)

    def open_navigator(self):
        self.page.hover(BBQCategoryPageLocators.ACCOUNT_NAVIGATOR)

    def click_heart_list_button(self):
        self.page.click(BBQCategoryPageLocators.HEART_LIST_BUTTON)