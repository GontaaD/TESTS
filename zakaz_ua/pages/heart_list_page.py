from zakaz_ua.locators.locators import HeartListPageLocators
from zakaz_ua.pages.base_page import BasePage

class HeartListPage(BasePage):
    def second_search_product_name(self):
        return self.get_text(HeartListPageLocators.PRODUCT_IN_LIST_TITLE)
