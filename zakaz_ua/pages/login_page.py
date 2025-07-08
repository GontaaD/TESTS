import allure
from playwright.sync_api import expect
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.locators.variables_page import Variables

class LoginPagelocators(BasePage):
    LOGIN_BUTTON = "//button[@data-marker='Header login']"
    NUMBER_INPUT = "//input[@class='form-control ']"
    PASSWORD_INPUT = "//input[@class='Input__field']"
    LOGIN_APPLY_BUTTON = "//button[@data-marker='Submit']"
    ERROR_LOGIN_MESSAGE = "//p[@data-testid='common-error']"

    def __init__(self, page):
        self.page = page

class LoginPage(BasePage):
    @allure.step("click login button")
    def click_login_button(self):
        self.page.click(LoginPagelocators.LOGIN_BUTTON)
        self.page.wait_for_timeout(300)

    @allure.step("fill number")
    def fill_number(self):
        number_input = self.page.locator(LoginPagelocators.NUMBER_INPUT)
        expect(number_input).to_be_visible()
        expect(number_input).to_be_enabled()
        number_input.fill("")
        self.page.wait_for_timeout(500)
        number_input.type(Variables.NUMBER, delay=100)
        self.page.wait_for_timeout(1000)
        final_value = number_input.input_value()
        assert final_value != "+380", f"Після введення по-символьно залишилось лише '+380', фактичне: {final_value}"
        expect(number_input).to_have_value("+380 (99) 795 20 94")

    @allure.step("fill password")
    def fill_password(self):
        password_input = self.page.locator(LoginPagelocators.PASSWORD_INPUT)
        expect(password_input).to_be_visible()
        expect(password_input).to_be_enabled()
        password_input.fill(Variables.PASSWORD)
        expect(password_input).to_have_value(Variables.PASSWORD)

    @allure.step("click confirm login button")
    def click_confirm_login_button(self):
        self.page.click(LoginPagelocators.LOGIN_APPLY_BUTTON)
        self.page.wait_for_timeout(300)

    @allure.step("login")
    def login(self):
        self.click_login_button()
        self.fill_number()
        self.fill_password()
        self.click_confirm_login_button()
        if self.page.is_visible(LoginPagelocators.ERROR_LOGIN_MESSAGE):
            raise AssertionError("Login failed: incorrect login or password")