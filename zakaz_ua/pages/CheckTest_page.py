import re
from allure import step
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.pages.list_page import ListPage
from zakaz_ua.pages.main_page import MainPage
from zakaz_ua.pages.login_page import LoginPage
from zakaz_ua.pages.BBQ_category_page import BBQPage
from zakaz_ua.pages.settings_page import SettingsPage
from zakaz_ua.pages.address_page import AddressPage
from zakaz_ua.locators.variables_page import Variables
from page_wrapper import PageWrapper as Pgw


def login_test_data():
    return [
        (Variables.NUMBER, Variables.PASSWORD, 'account_name_is_true'),
        (Variables.INCORRECT_NUMBER, Variables.INCORRECT_PASSWORD, 'error_login')
    ]

class CheckTestPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.bbq_page = BBQPage(page)
        self.list_page = ListPage(page)
        self.address_page = AddressPage(page)
        self.wrapper = Pgw(page)
        self.main_page = MainPage(page)
        self.settings_page = SettingsPage(page)
        self.login_page = LoginPage(page)

    @step("check all price in range")
    def check_all_prices_in_range(self, enter_min_price, enter_max_price):
        self.page.wait_for_timeout(500)
        price_blocks = self.bbq_page.price_block.get_locator
        price_blocks_count = price_blocks.count()

        for i in range(price_blocks_count):
            block = price_blocks.nth(i)

            start_text = block.locator(self.bbq_page.start_product_price.locator).text_content()
            start_val = self._parse_price(start_text)

            end_price_locator = block.locator(self.bbq_page.end_product_price.locator)
            end_val = None
            if end_price_locator.count() > 0:
                end_text = end_price_locator.text_content()
                end_val = self._parse_price(end_text)

            print(
                f"Product inspection {i}: start price = {start_val}, end price = {end_val if end_val is not None else 'absent'}"
            )

            if start_val == -1 or (end_val is not None and end_val == -1):
                print(f"Warning: price not recognized for product {i}, miss.")
                continue

            if end_val is None:
                end_val = start_val

            min_price = min(start_val, end_val)
            max_price = max(start_val, end_val)

            if not (max_price >= enter_min_price and min_price <= enter_max_price):
                raise AssertionError(
                    f"price range of the product [{min_price} - {max_price}] "
                    f"does not overlap the filter range [{enter_min_price} - {enter_max_price}]"
                    f"start text [{start_text}]"
                )

    @step("price adjustment method")
    def _parse_price(self, text):
        cleaned = text.strip().lstrip("-").strip()
        cleaned = re.sub(r"[^\d.,]", "", cleaned)
        cleaned = cleaned.replace(",", ".")
        try:
            return float(cleaned)
        except ValueError:
            return -1

    @step("check lists names")
    def rename_check(self, new_list_name, old_list_name):
        print(f"Name check: new name = '{new_list_name}', old name = '{old_list_name}'")
        assert new_list_name != old_list_name, (
            f"Error: the names are the same! new name = '{new_list_name}', old name = '{old_list_name}'"
        )

    @step("check create new list")
    def create_new_list_test(self, list_name):
        replace_list_name_locator = self.list_page.any_list.format(list_name=list_name)
        self.page.wait_for_timeout(500)
        list_count = replace_list_name_locator.count()
        print(f"Object count:'{replace_list_name_locator.locator}' '{list_count}' '{list_name}'")
        assert list_count != 0, (f"Object count:'{replace_list_name_locator.locator}' '{list_count}'")

    @step("check delete list")
    def delete_list_check(self, list_name):
        replace_list_name_locator = self.list_page.any_list.format(list_name=list_name)
        self.page.wait_for_timeout(500)
        list_count = replace_list_name_locator.count()
        print(f"Object count:'{replace_list_name_locator.locator}' '{list_count}' '{list_name}'")
        assert list_count == 0, (f"Object count:'{replace_list_name_locator.locator}' '{list_count}'")

    @step("like_availability_check")
    def like_availability_check (self):
        productTitle1 = self.bbq_page.search_product_name_in_catalog()
        productTitle2 = self.list_page.search_product_name_in_list()
        print(f"Name check: '{productTitle1}', '{productTitle2}'")
        assert productTitle1 == productTitle2, (
            f"Error: the name are different: '{productTitle1}', '{productTitle2}'"
        )

    @step("search field check")
    def search_field_check(self, part_of_the_product_name):
        self.page.wait_for_timeout(500)
        product_name_title = self.main_page.search_results_product.get_locator
        search_results_count = product_name_title.count()
        print(f"part of the product name: '{part_of_the_product_name}'")
        for i in range(search_results_count):
            with step(f"Product inspection {i}"):
                product_block = product_name_title.nth(i)
                product_name = product_block.text_content()

                product_name_lower = product_name.lower()
                part_lower = part_of_the_product_name.lower()
                print(
                    f"Product inspection {i}, product name: '{product_name}'"
                )
                if part_lower not in product_name_lower:
                    raise AssertionError(
                        f"Error: name: '{product_name}' dont have this part: '{part_of_the_product_name}'"
                    )

    @step("add personal data check")
    def add_personal_data_check(self,):
        saved_email = self.settings_page.save_email()
        saved_name = self.settings_page.save_name()
        saved_surname = self.settings_page.save_surname()
        email = Variables.TEST_GMAIL
        name = Variables.TEST_NAME
        surname = Variables.TEST_SURNAME
        print(
            f"Start personal data: Email:'{email}', Name:'{name}', Surname:'{surname}'\n"
            f"Added personal dara: Email:'{saved_email}', Name:'{saved_name}', Surname:'{saved_surname}'\n"
              )
        assert saved_email == email and saved_name == name and saved_surname == surname, (
            f"Error: the personal data are different:\n"
            f"Start personal data: Email:'{email}', Name:'{name}', Surname:'{surname}'\n"
            f"Added personal dara: Email:'{saved_email}', Name:'{saved_name}', Surname:'{saved_surname}'\n")

    @step("login check")
    def login_check(self, a, b, expected):
        self.login_page.login_button.click()
        self.login_page.fill_number(a)
        self.login_page.fill_password(b)
        self.login_page.login_apply_button.click()
        self.wrapper.wait_for_timeout(500)
        expected_metod = getattr(self.login_page, expected)
        result = expected_metod()
        print(f"Expected result: '{a}', '{b}', '{result}'")
        assert result is True
        if expected == "account_name_is_true":
            print("successful login")
        if expected == "error_login":
            print("failed login")

    @step("add address check")
    def compare_addresses(self, address_var: str, address_site: str) -> bool:
        parts_var = [self.normalize_part(p) for p in address_var.split(',')]
        parts_site = [self.normalize_part(p) for p in address_site.split(',')]
        for part in parts_var:
            if not any(part in site_part for site_part in parts_site):
                return False
        return True

    @step("normalize part")
    def normalize_part(self, part: str) -> str:
        return part.strip().lower()

    @step("add address check")
    def add_address_check(self):
        address_from_site = self.address_page.added_address.get_text()
        if self.compare_addresses(Variables.ADDRESS, address_from_site):
            print(f"The addresses match: '{Variables.ADDRESS}', '{address_from_site}'")
        else:
            print(f"Addresses are different: '{Variables.ADDRESS}', '{address_from_site}'")

