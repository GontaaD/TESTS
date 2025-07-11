from allure import step
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.locators.variables_page import Variables
from zakaz_ua.locators.BaseElement import BaseElement
from page_wrapper import PageWrapper as Pgw

class OpenAddressBar(BaseElement):
    @property
    def locator(self):
        return "//div[@data-marker='Address Management Bar']"

class AddedAddress(BaseElement):
    @property
    def locator(self):
        return "//div[@class='AddressManagementBar__delivery']"

class RegionButton(BaseElement):
    @property
    def locator(self):
        return "//div[@data-marker='Locality']"

class AddressButton(BaseElement):
    @property
    def locator(self):
        return "//div[@data-marker='Delivery address']//div[@class='SelectStyled__input']"

class SelectAddress(BaseElement):
    @property
    def format_locator(self):
        return "//*[text()='{variable}']//ancestor::div[contains(@id, 'react-select-3-option-')]"

class SelectCity(BaseElement):
    @property
    def format_locator(self):
        return "//*[text()='{variable}']//ancestor::div[contains(@id, 'react-select-2-option-')]"

class ConfirmAddressButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Confirm address']"

class AddressPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wrapper = Pgw(page)
        self.region_button = RegionButton(self.page)
        self.address_button = AddressButton(self.page)
        self.select_address_button = SelectAddress(self.page)
        self.select_city_button = SelectCity(self.page)
        self.confirm_address_button = ConfirmAddressButton(self.page)
        self.open_address_bar = OpenAddressBar(self.page)
        self.added_address = AddedAddress(self.page)

    @step("input address data")
    def select_address(self):
        self.open_address_bar.click()
        self.region_button.click()
        self.select_city_button.format(variable=Variables.CITY).click()
        self.address_button.click()
        self.address_button.type(Variables.ADDRESS, 20)
        self.wrapper.wait_for_timeout(1000)
        self.select_address_button.format(variable=Variables.ADDRESS).click()
        self.confirm_address_button.click()


