from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.pages.main_page import MainPage
import random
import string

class ListPageLocators:
    first_list_name = "Обрані"
    second_list_name = "лист123"

    RENAME_BUTTON = "//button[@data-marker='Change name']"
    MY_CREATED_LIST = "(//div[@class='css-1o947s6'])[1]"
    RENAME_MY_CREATED_LIST = "//div[@class='css-aqrc7q']"
    INPUT_LIST_NAME = "//input[@data-marker='List name']"
    APPLY_LIST_NAME_BUTTON = "//button[@data-marker='Save']"
    MY_CREATED_LIST_NAME = "(//p[@class='css-7m85l7'])[2]"
    PRODUCT_IN_LIST_TITLE = "(//div[@data-marker='Products List']//p[@class='CatalogProductTile__title'])[1]"
    FIRST_LIST_IN_CHANGE_LIST = "//*[text()='{first_list_name}']//ancestor::div[@class='css-1qx3rq8']"
    SECOND_LIST_IN_CHANGE_LIST = "//*[text()='{second_list_name}']//ancestor::div[@class='css-1l7o2vn']"
    SAVE_CHANGE_LIST_BUTTON = "//button[@data-marker='Save']"
    CHANGE_BUTTON = "//button[@data-marker='change']"
    CREATE_NEW_LIST_BUTTON = "//button[@data-marker='Open create list modal']"
    INPUT_NAME_NEW_CREATE_LIST = "//input[@data-marker='List name']"
    SAVE_NEW_CREATE_LIST_BUTTON = "//button[@data-marker='Save']"
    CREATED_NEW_LIST = "//*[text()='{list_name}']//ancestor::div[@class='css-1o947s6']"
    DELETE_LIST_BUTTON = "//button[@data-marker='Delete list']"
    APPLY_DELETE_LIST_BUTTON = "//button[@data-marker='Yes']"

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

    def input_name_for_new_list(self, list_name):
        self.page.fill(ListPageLocators.INPUT_NAME_NEW_CREATE_LIST, list_name)

    def save_new_list(self):
        self.page.click(ListPageLocators.SAVE_NEW_CREATE_LIST_BUTTON)

    def create_new_list(self, list_name):
        self.click_create_new_list()
        self.input_name_for_new_list(list_name)
        self.save_new_list()

    def generate_list_name(self):
        random_list_name = ''.join(random.choices(string.ascii_letters, k=5))
        return random_list_name

    def created_list_click(self, created_list_locator):
        created_list_locator.click()

    def delete_button_click(self):
        self.page.click(ListPageLocators.DELETE_LIST_BUTTON)

    def apply_delete_list_click(self):
        self.page.click(ListPageLocators.APPLY_DELETE_LIST_BUTTON)

    def delete_list(self, list_name):
        replace_list_name_locator = ListPageLocators.CREATED_NEW_LIST.format(list_name=list_name)
        created_list_locator = self.page.locator(replace_list_name_locator)
        self.created_list_click(created_list_locator)
        self.page.wait_for_timeout(500)
        self.delete_button_click()
        self.apply_delete_list_click()






