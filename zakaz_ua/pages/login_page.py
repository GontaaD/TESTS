from allure import step
from playwright.sync_api import expect
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.pages.main_page import MainPage
from helper.BaseElement import BaseElement
from page_wrapper import PageWrapper as Pgw

class LoginButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Header login']"

class NumberInput(BaseElement):
    @property
    def locator(self):
        return "//input[@class='form-control ']"

class PasswordInput(BaseElement):
    @property
    def locator(self):
        return "//input[@class='Input__field']"

class LoginApplyButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Submit']"

class ErrorLoginMessage(BaseElement):
    @property
    def locator(self):
        return "//p[@data-testid='common-error']"

class AccountName(BaseElement):
    @property
    def locator(self):
        return "//span[@data-testid='navigationUserName']"

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wrapper = Pgw(page)
        self.main_page = MainPage(page)
        self.login_button = LoginButton(page)
        self.number_input = NumberInput(page)
        self.password_input = PasswordInput(page)
        self.login_apply_button = LoginApplyButton(page)
        self.error_login_message = ErrorLoginMessage(page)
        self.account_name = AccountName(page)

    @step("fill number")
    def fill_number(self, number):
        expect(self.number_input.get_locator).to_be_enabled()
        self.number_input.clear()
        self.number_input.type(number, 30)
        final_value = self.number_input.input_value
        assert final_value != "+380", f"After character-by-character typing, only '+380' remained. Actual value: {final_value}"

    @step("fill password")
    def fill_password(self, password):
        expect(self.password_input.get_locator).to_be_enabled()
        self.password_input.fill(password)
        expect(self.password_input.get_locator).to_have_value(password)

    # @step("login")
    # def login(self):
    #     self.login_button.click()
    #     self.fill_number(Variables.NUMBER)
    #     self.fill_password(Variables.PASSWORD)
    #     self.login_apply_button.click()
    #     if self.error_login_message.is_visible():
    #         raise AssertionError("Login failed: incorrect login or password")

    @step("account name if visible")
    def is_account_name_is_true(self):
        self.account_name.wait_for(state="attached")
        return self.account_name.count() > 0

    @step("error login message is visible")
    def is_error_login(self):
        self.error_login_message.wait_for(state="visible", timeout=2000)
        return self.error_login_message.is_visible()