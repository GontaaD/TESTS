from zakaz_ua.locators.locators import LoginPagelocators
from zakaz_ua.locators.locators import LoginNumberAndPasswors
from zakaz_ua.pages.base_page import BasePage

class LoginPage(BasePage):
    def fill_number(self):
        self.page.fill(LoginPagelocators.NUMBER_INPUT, LoginNumberAndPasswors.NUMBER)

    def fill_password(self):
        self.page.fill(LoginPagelocators.PASSWORD_INPUT, LoginNumberAndPasswors.PASSWORD)

    def click_confirm_button(self):
        self.page.click(LoginPagelocators.LOGIN_BUTTON)