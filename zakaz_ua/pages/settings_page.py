from allure import step
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.locators.BaseElement import BaseElement
from zakaz_ua.locators.variables_page import Variables
from page_wrapper import PageWrapper as Pgw

class EmailInput(BaseElement):
    @property
    def locator(self):
        return "//input[@data-marker='email input']"

class NameInput(BaseElement):
    @property
    def locator(self):
        return "//input[@data-marker='name input']"

class SurnameInput(BaseElement):
    @property
    def locator(self):
        return "//input[@data-marker='surname input']"

class SavePersonalData(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='save personal data']"

class LogoButton(BaseElement):
    @property
    def locator(self):
        return "//a[@data-sentry-component='Logo']"

class SettingsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wrapper = Pgw(page)
        self.email_input = EmailInput(page)
        self.name_input = NameInput(page)
        self.surname_input = SurnameInput(page)
        self.save_personal_data = SavePersonalData(page)
        self.logo_button = LogoButton(page)

    @step("input personal data")
    def input_personal_data(self):
        self.save_personal_data.is_visible
        self.save_personal_data.scroll_into_view_if_needed()
        self.email_input.clear()
        self.email_input.fill(Variables.TEST_GMAIL)
        self.name_input.clear()
        self.name_input.fill(Variables.TEST_NAME)
        self.surname_input.clear()
        self.surname_input.fill(Variables.TEST_SURNAME)
        self.save_personal_data.click()
        self.logo_button.click()

    @step("input old personal data")
    def input_old_personal_data(self):
        self.save_personal_data.is_visible
        self.save_personal_data.scroll_into_view_if_needed()
        self.email_input.clear()
        self.email_input.fill(Variables.GMAIL)
        self.name_input.clear()
        self.name_input.fill(Variables.NAME)
        self.surname_input.clear()
        self.surname_input.fill(Variables.SURNAME)
        self.save_personal_data.click()

    @step("save email")
    def save_email(self):
        return self.email_input.input_value

    @step("save name")
    def save_name(self):
        return self.name_input.input_value

    @step("save surname")
    def save_surname(self):
        return self.surname_input.input_value

