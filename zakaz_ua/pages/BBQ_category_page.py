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

    def open_heart_list(self):
        self.open_navigator()
        self.click_heart_list_button()

    def set_max_price(self, enter_max_price):
        self.page.fill(BBQCategoryPageLocators.MAX_PRICE_FILTER, str(enter_max_price))

    def set_min_price(self, enter_min_price):
        self.page.fill(BBQCategoryPageLocators.MIN_PRICE_FILTER, str(enter_min_price))

    def click_filter_apply_button(self):
        self.page.click(BBQCategoryPageLocators.FILTER_APPLY_BUTTON)
        self.page.wait_for_timeout(1000)

    def fill_price_filter(self, enter_min_price, enter_max_price):
        self.set_max_price(enter_max_price)
        self.set_min_price(enter_min_price)
        self.click_filter_apply_button()
