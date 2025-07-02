from zakaz_ua.locators.locators import ListPageLocators
from zakaz_ua.pages.base_page import BasePage

class ListPage(BasePage):
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

    def rename_check(self, new_list_name, old_list_name):
        print(f"Перевірка назв: нова назва = '{new_list_name}', стара назва = '{old_list_name}'")
        assert new_list_name != old_list_name, (
            f"Помилка: назви списків збігаються! нова назва = '{new_list_name}', стара назва = '{old_list_name}'"
        )


