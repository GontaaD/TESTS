from allure import step
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.locators.BaseElement import BaseElement
from page_wrapper import PageWrapper as Pgw

class LikeButton(BaseElement):
    @property
    def locator(self):
        return "(//button[@data-marker='Favorite button'])[1]"

class ProductTitle(BaseElement):
    @property
    def locator(self):
        return "(//p[@class='CatalogProductTile__title'])[1]"

class MinPriceFilter(BaseElement):
    @property
    def locator(self):
        return "//input[@data-testid='price-min']"

class MaxPriceFilter(BaseElement):
    @property
    def locator(self):
     return "//input[@data-testid='price-max']"

class StartProductPrice(BaseElement):
    @property
    def locator(self):
        return "//span[@class='PricesRange__start']"

class EndProductPrice(BaseElement):
    @property
    def locator(self):
        return "//span[@class='PricesRange__end']"

class FilterApplyButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Filter Price OK']"

class PriceBlock(BaseElement):
    @property
    def locator(self):
        return "//span[@data-sentry-component='PriceRange']"

class BBQPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wrapper = Pgw(page)
        self.like_button = LikeButton(self.page)
        self.product_title = ProductTitle(self.page)
        self.min_price_filter = MinPriceFilter(self.page)
        self.max_price_filter = MaxPriceFilter(self.page)
        self.start_product_price = StartProductPrice(self.page)
        self.end_product_price = EndProductPrice(self.page)
        self.filter_apply_button = FilterApplyButton(self.page)
        self.price_block = PriceBlock(self.page)

    @step("click heart button")
    def click_heart_button(self):
        self.like_button.click()

    @step("search product name in catalog")
    def search_product_name_in_catalog(self):
        return self.product_title.get_text()

    @step("set price filter")
    def set_price_filter(self, enter_min_price, enter_max_price):
        self.max_price_filter.fill(str(enter_max_price))
        self.min_price_filter.fill(str(enter_min_price))
        self.filter_apply_button.click()
