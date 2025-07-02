from zakaz_ua.locators.locators import LoginPagelocators
from zakaz_ua.pages.base_page import BasePage

class LoginNumberAndPassword:
    NUMBER = "997952094"
    PASSWORD = "198595"

class LoginPage(BasePage):

    def click_login(self):
        self.page.click(LoginPagelocators.LOGIN_BUTTON)

    def fill_number(self):
        self.page.wait_for_selector(LoginPagelocators.NUMBER_INPUT)
        self.page.fill(LoginPagelocators.NUMBER_INPUT, LoginNumberAndPassword.NUMBER)

    def fill_password(self):
        self.page.fill(LoginPagelocators.PASSWORD_INPUT, LoginNumberAndPassword.PASSWORD)

    def click_confirm_button(self):
        self.page.click(LoginPagelocators.LOGIN_APPLY)

    def login(self):
        self.click_login()
        self.page.wait_for_timeout(300)
        self.fill_number()
        self.page.wait_for_timeout(300)
        self.fill_password()
        self.page.wait_for_timeout(300)
        self.click_confirm_button()