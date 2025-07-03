from zakaz_ua.locators.locators import LoginPagelocators
from zakaz_ua.pages.base_page import BasePage

class LoginNumberAndPassword:
    NUMBER = "997952094"
    PASSWORD = "198595"

class LoginPage(BasePage):
    def click_login_button(self):
        self.page.click(LoginPagelocators.LOGIN_BUTTON)

    def fill_number(self):
        self.page.wait_for_selector(LoginPagelocators.NUMBER_INPUT)
        self.page.fill(LoginPagelocators.NUMBER_INPUT, LoginNumberAndPassword.NUMBER)

    def fill_password(self):
        self.page.fill(LoginPagelocators.PASSWORD_INPUT, LoginNumberAndPassword.PASSWORD)

    def click_confirm_login_button(self):
        self.page.click(LoginPagelocators.LOGIN_APPLY)

    def login(self):
        basepage = BasePage(self.page)
        self.click_login_button()
        basepage.is_visible(LoginPagelocators.NUMBER_INPUT)
        self.fill_number()
        self.page.wait_for_timeout(300)
        self.fill_password()
        self.page.wait_for_timeout(300)
        self.click_confirm_login_button()