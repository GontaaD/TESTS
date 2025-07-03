from zakaz_ua.locators.locators import ListPageLocators
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.pages.main_page import MainPage

class ListPage(BasePage):
    def search_product_name_in_list(self):
        return self.get_text(ListPageLocators.PRODUCT_IN_LIST_TITLE)

    def open_my_cerated_list(self):
        self.page.click(ListPageLocators.MY_CREATED_LIST)

    def click_rename_button(self):
        self.page.click(ListPageLocators.RENAME_BUTTON)

    def save_old_list_name(self):
        return self.page.locator(ListPageLocators.MY_CREATED_LIST_NAME).text_content()

    def clear_input_list_name(self):
        self.page.fill(ListPageLocators.INPUT_LIST_NAME, "")

    def input_list_name(self, new_list_name):
        self.page.fill(ListPageLocators.INPUT_LIST_NAME, str(new_list_name))

    def input_old_list_name(self, start_list_name):
        self.page.fill(ListPageLocators.INPUT_LIST_NAME, str(start_list_name))

    def click_apply_list_name(self):
        self.page.click(ListPageLocators.APPLY_LIST_NAME_BUTTON)

    def rename_list(self, new_list_name):
        self.open_my_cerated_list()
        self.click_rename_button()
        self.page.wait_for_timeout(500)
        self.clear_input_list_name()
        self.input_list_name(new_list_name)
        self.click_apply_list_name()
        self.page.wait_for_timeout(500)

        #back old name
    def open_rename_my_cerated_list(self):
        self.page.click(ListPageLocators.RENAME_MY_CREATED_LIST)

    def back_old_list_name(self, start_list_name):
        self.open_rename_my_cerated_list()
        self.click_rename_button()
        self.page.wait_for_timeout(300)
        self.clear_input_list_name()
        self.input_old_list_name(start_list_name)
        self.click_apply_list_name()

    def click_change_list_button(self):
        self.page.click(ListPageLocators.CHANGE_BUTTON)

    def click_first_list_for_change(self):
        self.page.click(ListPageLocators.FIRST_LIST_IN_CHANGE_LIST)

    def click_second_list_for_change(self):
        self.page.click(ListPageLocators.SECOND_LIST_IN_CHANGE_LIST)

    def save_change_list(self):
        self.page.click(ListPageLocators.SAVE_CHANGE_LIST_BUTTON)

    def change_list(self):
        self.click_change_list_button()
        self.page.wait_for_timeout(500)
        self.click_first_list_for_change()
        self.page.wait_for_timeout(500)
        self.click_second_list_for_change()
        self.page.wait_for_timeout(500)
        self.save_change_list()

    def check_product_in_second_list(self):
        mainpage = MainPage(self.page)
        mainpage.open_list_menu()
        self.open_my_cerated_list()

    def click_create_new_list(self):
        self.page.click(ListPageLocators.CREATE_NEW_LIST_BUTTON)

    def input_name_for_new_list(self, name_for_new_list):
        self.page.fill(ListPageLocators.INPUT_NAME_NEW_CREATE_LIST, str(name_for_new_list))

    def save_new_list(self):
        self.page.click(ListPageLocators.SAVE_NEW_CREATE_LIST_BUTTON)

    def create_new_list(self, name_for_new_list):
        self.click_create_new_list()
        self.input_name_for_new_list(name_for_new_list)
        self.save_new_list()




