from zakaz_ua.locators.locators import BBQCategoryPageLocators
from zakaz_ua.pages.base_page import BasePage

class BBQPage(BasePage):
    def click_heart_button(self):
        self.page.click(BBQCategoryPageLocators.HEART_BUTTON)

    def search_product_name_in_catalog(self):
        return self.get_text(BBQCategoryPageLocators.PRODUCT_TITLE)

    def set_max_price_in_filter(self, enter_max_price):
        self.page.fill(BBQCategoryPageLocators.MAX_PRICE_FILTER, str(enter_max_price))

    def set_min_price_in_filter(self, enter_min_price):
        self.page.fill(BBQCategoryPageLocators.MIN_PRICE_FILTER, str(enter_min_price))

    def click_filter_apply_button(self):
        self.page.click(BBQCategoryPageLocators.FILTER_APPLY_BUTTON)
        self.page.wait_for_timeout(1000)

    def fill_price_filter(self, enter_min_price, enter_max_price):
        self.set_max_price_in_filter(enter_max_price)
        self.set_min_price_in_filter(enter_min_price)
        self.click_filter_apply_button()
