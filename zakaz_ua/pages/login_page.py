from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.locators.variables_page import LoginNumberAndPassword

class LoginPagelocators:
    LOGIN_BUTTON = "//button[contains(@class, 'LoginButton css-hnx7nu')]"
    NUMBER_INPUT = "//input[@class='form-control ']"
    PASSWORD_INPUT = "//input[@class='Input__field']"
    LOGIN_APPLY = "//button[@class='css-xdkem']"

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