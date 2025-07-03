from zakaz_ua.locators.locators import MainPagelocators
from zakaz_ua.pages.base_page import BasePage

class MainPage(BasePage):
    def click_category_button(self):
        self.page.click(MainPagelocators.CATEGORY_BUTTON)

    def click_bbq_button(self):
        self.page.click(MainPagelocators.BBQ_CATEGORY_BUTTON)

    def open_bbq_category(self):
        self.click_category_button()
        self.click_bbq_button()

    def open_account_navigator(self):
        self.page.hover(MainPagelocators.ACCOUNT_NAVIGATOR)

    def click_to_list_menu(self):
        self.page.click(MainPagelocators.LIST_MENU)

    def open_list_menu(self):
        self.open_account_navigator()
        self.page.wait_for_timeout(500)
        self.click_to_list_menu()

        #remove like
    def remove_like(self):
        self.page.click(MainPagelocators.LIKE_BUTTON)




