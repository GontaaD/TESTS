import random
import string
from allure import step
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.pages.main_page import MainPage
from zakaz_ua.locators.BaseElement import BaseElement
from page_wrapper import PageWrapper as Pgw

class RenameButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Change name']"

class AnyList(BaseElement):
    @property
    def format_locator(self):
        return "//*[text()='{list_name}']//ancestor::p[@data-sentry-element='StyledComponent']"

class InputListName(BaseElement):
    @property
    def locator(self):
        return "//input[@data-marker='List name']"

class ApplyListNameButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Save']"

class ProductInListName(BaseElement):
    @property
    def locator(self):
        return "(//p[@class='CatalogProductTile__title'])"

class SaveChangeListButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Save']"

class ChangeListButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='change']"

class CreateNewListButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Open create list modal']"

class InputNameNewCreateList(BaseElement):
    @property
    def locator(self):
        return "//input[@data-marker='List name']"

class SaveNewCreateListButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Save']"

class DeleteListButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Delete list']"

class ApplyDeleteListButton(BaseElement):
    @property
    def locator(self):
        return "//button[@data-marker='Yes']"

class SelectedListInChangeList(BaseElement):
    @property
    def locator(self):
        return "//div[@aria-checked='true']"

class ListPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wrapper = Pgw(page)
        self.rename_button = RenameButton(self.page)
        self.any_list = AnyList(self.page)
        self.main_page = MainPage(self.page)
        self.input_list_name = InputListName(self.page)
        self.apply_list_name = ApplyListNameButton(self.page)
        self.product_in_list_name = ProductInListName(self.page)
        self.save_change_list_button = SaveChangeListButton(self.page)
        self.change_list_button = ChangeListButton(self.page)
        self.create_new_list_button = CreateNewListButton(self.page)
        self.input_name_new_created_list = InputNameNewCreateList(self.page)
        self.save_new_created_list_button = SaveNewCreateListButton(self.page)
        self.delete_list_button = DeleteListButton(self.page)
        self.apply_delete_list_button = ApplyDeleteListButton(self.page)
        self.selected_list_in_change_list = SelectedListInChangeList(self.page)

    @step("search product name in list")
    def search_product_name_in_list(self):
        return self.product_in_list_name.wait_for(state="visible", timeout=1000).get_text()

    @step("open my created list")
    def open_my_created_list(self,list_name):
        self.any_list.format(list_name=list_name).wait_for(state="visible", timeout=3000).click()
        self.delete_list_button.wait_for(state="visible", timeout=3000)

    @step("save old list name")
    def save_old_list_name(self, old_list_name):
        return self.any_list.format(list_name=old_list_name).get_text()

    @step("save new list name")
    def save_new_list_name(self, new_list_name):
        return self.any_list.format(list_name=new_list_name).get_text()

    @step("clear input list name")
    def clear_input_list_name(self):
        self.input_list_name.wait_for(state="visible").clear()

    @step("click apply list name")
    def click_apply_list_name(self):
        self.apply_list_name.click()

    @step("rename list")
    def rename_list(self, old_list_name, new_list_name):
        self.open_my_created_list(old_list_name)
        self.rename_button.click()
        self.clear_input_list_name()
        self.input_list_name.fill(new_list_name)
        self.click_apply_list_name()

    @step("back old list name")
    def back_old_list_name(self, old_list_name, new_list_name):
        self.any_list.format(list_name=new_list_name).click()
        self.rename_button.click()
        self.clear_input_list_name()
        self.input_list_name.fill(old_list_name)
        self.click_apply_list_name()

    @step("change list")
    def change_list(self, first_list_name, second_list_name):
        self.change_list_button.wait_for(state="visible", timeout=1000).click()
        self.selected_list_in_change_list.wait_for(state="visible", timeout=1000)
        self.any_list.format(list_name=first_list_name).wait_for(state="visible").click()
        self.any_list.format(list_name=second_list_name).wait_for(state="visible").click()
        self.save_change_list_button.wait_for(state="visible").click()

    @step("check product in second list")
    def open_another_list(self, second_list_name):
        self.main_page.open_list_menu()
        self.open_my_created_list(second_list_name)

    @step("create new list")
    def create_new_list(self, list_name):
        self.create_new_list_button.click()
        self.input_name_new_created_list.fill(list_name)
        self.save_new_created_list_button.click()

    @step("generate list name")
    def generate_list_name(self):
        random_list_name = ''.join(random.choices(string.ascii_letters, k=5))
        return random_list_name

    @step("delete list")
    def delete_list(self, list_name):
        self.any_list.format(list_name=list_name).wait_for(state="visible").click()
        self.delete_list_button.wait_for(state="visible").click()
        self.apply_delete_list_button.click()
        self.any_list.format(list_name=list_name).wait_for(state="hidden")