from allure import step
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.locators.BaseElement import BaseElement
from page_wrapper import PageWrapper as Pgw

class SubcategoryButton(BaseElement):
    @property
    def format_locator(self):
        return "//*[text()='{category_name}']//ancestor::a[@data-sentry-component='LinkWithLoading']"

class ProductNameTitle(BaseElement):
    @property
    def locator(self):
        return "//p[@class='CatalogProductTile__title']"

class SubcategoryNameTitle(BaseElement):
    @property
    def format_locator(self):
        return "//*[text()='{category_name}']//ancestor::h1[@data-sentry-element='StyledComponent']"

class EggAndMilkCategoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wrapper = Pgw(page)
        self.subcategory_button = SubcategoryButton(self.page)
        self.product_name_title = ProductNameTitle(self.page)
        self.subcategory_name_title = SubcategoryNameTitle(self.page)

    @step("open egg subcategory")
    def open_subcategory(self, subcategory_name):
        self.subcategory_button.format(category_name=subcategory_name).wait_for(state="visible").click()