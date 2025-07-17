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

class InputPostalMachineCity(BaseElement):
    @property
    def locator(self):
        return "//div[@data-marker='City']"

class SelectPostalMachineCity(BaseElement):
    @property
    def format_locator(self):
        return "//*[text()='{variable}']//ancestor::div[contains(@id, 'react-select-4-option-')]"

class SelectPostalMachineAddress(BaseElement):
    @property
    def format_locator(self):
        return "//*[contains(text(), '{variable}')]//ancestor::div[contains(@id, 'react-select-5-option-')]"

class NovaPoshta(BaseElement):
    @property
    def locator(self):
        return "//li[@data-marker='Nova Poshta']"

class PostalMachineButton(BaseElement):
    @property
    def locator(self):
        return "//input[@id='np_by_postomat-np_by_postomat']"

class InputPostalMachineAddress(BaseElement):
    @property
    def locator(self):
        return "//div[@data-marker='Branch Number']"

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
        self.postal_machine_button = PostalMachineButton(self.page)
        self.nova_poshta = NovaPoshta(self.page)
        self.select_postal_machine_address = SelectPostalMachineAddress(self.page)
        self.input_postal_machine_address = InputPostalMachineAddress(self.page)
        self.input_postal_machine_city = InputPostalMachineCity(self.page)
        self.select_postal_machine_city = SelectPostalMachineCity(self.page)


    @step("input address data")
    def set_courier_address(self):
        self.open_address_bar.click()
        self.region_button.click()
        self.select_city_button.format(variable=Variables.COURIER_CITY).click()
        self.address_button.click()
        self.address_button.type(Variables.ADDRESS, 20)
        self.select_address_button.format(variable=Variables.ADDRESS).wait_for(state="visible").click()
        self.confirm_address_button.click()

    @step("select postal machine address")
    def set_postal_machine_address(self):
        self.open_address_bar.click()
        self.nova_poshta.wait_for(state="visible", timeout=3000).click()
        self.postal_machine_button.wait_for(state="visible").click()
        self.input_postal_machine_city.wait_for(state="visible").click()
        self.input_postal_machine_city.type(Variables.POSTAL_MACHINE_CITY, 20)
        self.select_postal_machine_city.format(variable=Variables.POSTAL_MACHINE_CITY).wait_for(state="visible", timeout=1000).click()
        self.input_postal_machine_address.wait_for(state="visible").click()
        self.input_postal_machine_address.wait_for(state="visible").type(Variables.POSTAL_MACHINE_ADDRESS, 20)
        self.select_postal_machine_address.format(variable=Variables.POSTAL_MACHINE_ADDRESS).wait_for(state="visible", timeout=1000).click()
        self.confirm_address_button.click()

