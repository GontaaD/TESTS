import allure
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.pages.main_page import MainPage
import random
import string

class ListPageLocators(BasePage):
    RENAME_BUTTON = "//button[@data-marker='Change name']"
    MY_CREATED_LIST = "//*[text()='{list_name}']//ancestor::p[@data-sentry-element='StyledComponent']"
    INPUT_LIST_NAME = "//input[@data-marker='List name']"
    APPLY_LIST_NAME_BUTTON = "//button[@data-marker='Save']"
    PRODUCT_IN_LIST_TITLE = "(//p[@class='CatalogProductTile__title'])[1]"
    LIST_IN_CHANGE_LIST = "//*[text()='{list_name}']//ancestor::p[@data-sentry-element='StyledComponent']"
    SAVE_CHANGE_LIST_BUTTON = "//button[@data-marker='Save']"
    CHANGE_LIST_BUTTON = "//button[@data-marker='change']"
    CREATE_NEW_LIST_BUTTON = "//button[@data-marker='Open create list modal']"
    INPUT_NAME_NEW_CREATE_LIST = "//input[@data-marker='List name']"
    SAVE_NEW_CREATE_LIST_BUTTON = "//button[@data-marker='Save']"
    CREATED_NEW_LIST = "//*[text()='{list_name}']//ancestor::p[@data-sentry-element='StyledComponent']"
    DELETE_LIST_BUTTON = "//button[@data-marker='Delete list']"
    APPLY_DELETE_LIST_BUTTON = "//button[@data-marker='Yes']"

    def __init__(self, page):
        self.page = page

class ApplyDeleListButton(BasePage):
    @property
    def locator(self):
        return f"//button[@data-marker='Yes']"

class ListPage(BasePage):
    @allure.step("search product name in list")
    def search_product_name_in_list(self):
        return self.get_text(ListPageLocators.PRODUCT_IN_LIST_TITLE)

    @allure.step("open my created list")
    def open_my_created_list(self,old_list_name):
        self.page.click(ListPageLocators.MY_CREATED_LIST.format(list_name=old_list_name))

    @allure.step("click rename button")
    def click_rename_button(self):
        self.page.click(ListPageLocators.RENAME_BUTTON)

    @allure.step("save old list name")
    def save_old_list_name(self, old_list_name):
        return self.page.locator(ListPageLocators.MY_CREATED_LIST.format(list_name=old_list_name)).text_content()

    @allure.step("clear input list name")
    def clear_input_list_name(self):
        self.page.fill(ListPageLocators.INPUT_LIST_NAME, "")

    @allure.step("input new list name")
    def input_new_list_name(self, new_list_name):
        self.page.fill(ListPageLocators.INPUT_LIST_NAME, str(new_list_name))

    @allure.step("input old list name")
    def input_old_list_name(self, old_list_name):
        self.page.fill(ListPageLocators.INPUT_LIST_NAME, str(old_list_name))

    @allure.step("click apply list name")
    def click_apply_list_name(self):
        self.page.click(ListPageLocators.APPLY_LIST_NAME_BUTTON)

    @allure.step("rename list")
    def rename_list(self, old_list_name, new_list_name):
        self.open_my_created_list(old_list_name)
        self.click_rename_button()
        self.page.wait_for_timeout(500)
        self.clear_input_list_name()
        self.input_new_list_name(new_list_name)
        self.click_apply_list_name()
        self.page.wait_for_timeout(500)

    @allure.step("open my renamed list")
    def open_my_renamed_list(self, new_list_name):
        self.page.click(ListPageLocators.MY_CREATED_LIST.format(list_name=new_list_name))

    @allure.step("back old list name")
    def back_old_list_name(self, old_list_name, new_list_name):
        self.open_my_renamed_list(new_list_name)
        self.click_rename_button()
        self.page.wait_for_timeout(300)
        self.clear_input_list_name()
        self.input_old_list_name(old_list_name)
        self.click_apply_list_name()

    @allure.step("click change list button")
    def click_change_list_button(self):
        self.page.click(ListPageLocators.CHANGE_LIST_BUTTON)

    @allure.step("click first list for change")
    def click_first_list_for_change(self, first_list_name):
        self.page.click(ListPageLocators.LIST_IN_CHANGE_LIST.format(list_name=first_list_name))

    @allure.step("click second list for change")
    def click_second_list_for_change(self, second_list_name):
        self.page.click(ListPageLocators.LIST_IN_CHANGE_LIST.format(list_name=second_list_name))

    @allure.step("save change list button")
    def click_save_change_list_button(self):
        self.page.click(ListPageLocators.SAVE_CHANGE_LIST_BUTTON)

    @allure.step("change list")
    def change_list(self, first_list_name, second_list_name):
        self.click_change_list_button()
        self.page.wait_for_timeout(500)
        self.click_first_list_for_change(first_list_name)
        self.page.wait_for_timeout(500)
        self.click_second_list_for_change(second_list_name)
        self.page.wait_for_timeout(500)
        self.click_save_change_list_button()

    @allure.step("check product in second list")
    def check_product_in_second_list(self, second_list_name):
        mainpage = MainPage(self.page)
        mainpage.open_list_menu()
        self.open_my_created_list(second_list_name)

    @allure.step("click create new list button")
    def click_create_new_list_button(self):
        self.page.click(ListPageLocators.CREATE_NEW_LIST_BUTTON)

    @allure.step("input name for new list")
    def input_name_for_new_list(self, list_name):
        self.page.fill(ListPageLocators.INPUT_NAME_NEW_CREATE_LIST, list_name)

    @allure.step("click save new list button")
    def click_save_new_list_button(self):
        self.page.click(ListPageLocators.SAVE_NEW_CREATE_LIST_BUTTON)

    @allure.step("create new list")
    def create_new_list(self, list_name):
        self.click_create_new_list_button()
        self.input_name_for_new_list(list_name)
        self.click_save_new_list_button()

    @allure.step("generate list name")
    def generate_list_name(self):
        random_list_name = ''.join(random.choices(string.ascii_letters, k=5))
        return random_list_name

    @allure.step("click in created list")
    def click_created_list(self, created_list_locator):
        created_list_locator.click()

    @allure.step("click delete list button")
    def click_delete_button(self):
        self.page.click(ListPageLocators.DELETE_LIST_BUTTON)

    @allure.step("click apply delete list button")
    def click_apply_delete_list_button(self):
        self.page.click(ListPageLocators.APPLY_DELETE_LIST_BUTTON)

    @allure.step("delete list")
    def delete_list(self, list_name):
        replace_list_name_locator = ListPageLocators.CREATED_NEW_LIST.format(list_name=list_name)
        created_list_locator = self.page.locator(replace_list_name_locator)
        self.click_created_list(created_list_locator)
        self.page.wait_for_timeout(500)
        self.click_delete_button()
        self.click_apply_delete_list_button()