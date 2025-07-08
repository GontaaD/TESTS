import allure
from zakaz_ua.pages.base_page import BasePage

class BBQCategoryPageLocators(BasePage):
    LIKE_BUTTON = "(//button[@data-marker='Favorite button'])[1]"
    PRODUCT_TITLE = "(//p[@class='CatalogProductTile__title'])[1]"
    MIN_PRICE_FILTER = "//input[@data-testid='price-min']"
    MAX_PRICE_FILTER = "//input[@data-testid='price-max']"
    START_PRODUCT_PRICE = "//span[@class='PricesRange__start']"
    END_PRODUCT_PRICE = "//span[@class='PricesRange__end']"
    FILTER_APPLY_BUTTON = "//button[@data-marker='Filter Price OK']"
    PRICE_BLOCK = "//span[@data-sentry-component='PriceRange']"

    def __init__(self, page):
        self.page = page

class BBQPage(BasePage):
    @allure.step("click heart button")
    def click_heart_button(self):
        self.page.click(BBQCategoryPageLocators.LIKE_BUTTON)

    @allure.step("search product name in catalog")
    def search_product_name_in_catalog(self):
        return self.get_text(BBQCategoryPageLocators.PRODUCT_TITLE)

    @allure.step("set max price in filter")
    def set_max_price_in_filter(self, enter_max_price):
        self.page.fill(BBQCategoryPageLocators.MAX_PRICE_FILTER, str(enter_max_price))

    @allure.step("set min price in filter")
    def set_min_price_in_filter(self, enter_min_price):
        self.page.fill(BBQCategoryPageLocators.MIN_PRICE_FILTER, str(enter_min_price))

    @allure.step("click filter apply button")
    def click_filter_apply_button(self):
        self.page.click(BBQCategoryPageLocators.FILTER_APPLY_BUTTON)
        self.page.wait_for_timeout(1000)

    @allure.step("set price filter")
    def set_price_filter(self, enter_min_price, enter_max_price):
        self.set_max_price_in_filter(enter_max_price)
        self.set_min_price_in_filter(enter_min_price)
        self.click_filter_apply_button()
