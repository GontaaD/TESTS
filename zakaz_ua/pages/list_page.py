from zakaz_ua.locators.locators import ListPageLocators
from zakaz_ua.pages.base_page import BasePage

class ListPage(BasePage):
    def second_search_product_name(self):
        return self.get_text(ListPageLocators.PRODUCT_IN_LIST_TITLE)

    def open_list(self):
        self.page.click(ListPageLocators.LIST)

    def click_rename_button(self):
        self.page.click(ListPageLocators.RENAME_BUTTON)

    def save_old_list_name(self):
        return self.page.locator(ListPageLocators.LIST_NAME).text_content()

    def clear_input(self):
        self.page.fill(ListPageLocators.INPUT_LIST_NAME, "")

    def input_list_name(self, new_list_name):
        self.page.fill(ListPageLocators.INPUT_LIST_NAME, str(new_list_name))

    def click_apply_list_name(self):
        self.page.click(ListPageLocators.APPLY_LIST_NAME_BUTTON)

    def rename_list(self, new_list_name):
        self.open_list()
        self.click_rename_button()
        self.page.wait_for_timeout(500)
        self.clear_input()
        self.input_list_name(new_list_name)
        self.click_apply_list_name()
        self.page.wait_for_timeout(500)


