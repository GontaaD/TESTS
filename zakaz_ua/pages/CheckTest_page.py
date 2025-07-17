import re
from allure import step
from zakaz_ua.pages.base_page import BasePage
from zakaz_ua.pages.list_page import ListPage
from zakaz_ua.pages.main_page import MainPage
from zakaz_ua.pages.login_page import LoginPage
from zakaz_ua.pages.BBQ_category_page import BBQPage
from zakaz_ua.pages.settings_page import SettingsPage
from zakaz_ua.pages.address_page import AddressPage
from zakaz_ua.pages.vacancies_page import VacanciesPage
from zakaz_ua.locators.variables_page import Variables
from zakaz_ua.pages.egg_and_milk_category_page import EggAndMilkCategoryPage
from page_wrapper import PageWrapper as Pgw

def login_test_data():
    return [
        (Variables.NUMBER, Variables.PASSWORD, 'is_account_name_is_true'),
        (Variables.INCORRECT_NUMBER, Variables.INCORRECT_PASSWORD, 'is_error_login')
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
        self.egg_and_milk_category_page = EggAndMilkCategoryPage(page)

    @step("check all price in range")
    def check_all_prices_in_range(self, enter_min_price, enter_max_price):
        self.bbq_page.clear_all_filters_button.wait_for(state="visible")
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
        print("All products fall under the filter")

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
        print("Renaming the list was successful")

    @step("check create new list")
    def create_new_list_test(self, list_name):
        replace_list_name_locator = self.list_page.any_list.format(list_name=list_name).wait_for(state="visible")
        list_count = replace_list_name_locator.count()
        print(f"Object count:'{replace_list_name_locator.locator}' '{list_count}' '{list_name}'")
        assert list_count != 0, (f"Object count:'{replace_list_name_locator.locator}' '{list_count}'")
        print("New list created successfully")

    @step("check delete list")
    def delete_list_check(self, list_name):
        replace_list_name_locator = self.list_page.any_list.format(list_name=list_name).wait_for(state="detached")
        list_count = replace_list_name_locator.count()
        print(f"Object count:'{replace_list_name_locator.locator}' '{list_count}' '{list_name}'")
        assert list_count == 0, (f"Object count:'{replace_list_name_locator.locator}' '{list_count}'")
        print("List deletion successful")

    @step("like_availability_check")
    def like_availability_check(self, productTitle1, productTitle2):
        print(f"Name check: '{productTitle1}', '{productTitle2}'")
        if productTitle1 == productTitle2:
            print("Having a like is successful")
        else:
            raise AssertionError(f"Error: the name are different: '{productTitle1}', '{productTitle2}'")

    @step("search part field check")
    def search_part_field_check(self, part_of_the_product_name):
        self.main_page.search_results_product.wait_for(state="visible")
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
        print("All products have part of the name")

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
        print("Adding personal data successful")

    @step("login check")
    def login_check(self, a, b, expected):
        self.login_page.login_button.click()
        self.login_page.fill_number(a)
        self.login_page.fill_password(b)
        self.login_page.login_apply_button.click()
        expected_metod = getattr(self.login_page, expected)
        is_result = expected_metod()
        print(f"Expected result: '{a}', '{b}', '{is_result}'")
        assert is_result is True
        if expected == "is_account_name_is_true":
            print("successful login")
        if expected == "is_error_login":
            print("failed login")

    @step("add address check")
    def is_compare_addresses(self, address_var: str, address_site: str) -> bool:
        parts_var = [self.normalize_part(p) for p in address_var.split(',')]
        parts_site = [self.normalize_part(p) for p in address_site.split(',')]
        for part in parts_var:
            if not any(part in site_part for site_part in parts_site):
                return False
        return True

    @step("normalize part")
    def normalize_part(self, part: str) -> str:
        return part.strip().lower()

    @step("add courier address check")
    def add_courier_address_check(self):
        address_from_site = self.address_page.added_address.get_text()
        if self.is_compare_addresses(Variables.ADDRESS, address_from_site):
            print(f"The addresses match: '{Variables.ADDRESS}', '{address_from_site}'")
        else:
            raise AssertionError(f"Addresses are different: '{Variables.ADDRESS}', '{address_from_site}'")

    @step("vacancies filter city name check")
    def vacancies_filter_check(self, city_name):
        with step("open vacancies page"):
            with self.page.context.expect_page() as new_page_info:
                self.main_page.vacancies_page_click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        vacancies_page = VacanciesPage(new_page)
        with step("filter city chose"):
            vacancies_page.city_filter_click(city_name)
        self.wrapper.wait_for_timeout(1000)
        vacancies = vacancies_page.vacancies_block.get_locator
        vacancies_count = vacancies.count()
        cityes = []
        try:
            with step("show more button click"):
                vacancies_page.show_more_button.wait_for(state="visible", timeout=2000)
                vacancies_page.show_more_button.scroll_into_view_if_needed()
                vacancies_page.show_more_button.click()
                vacancies.nth(vacancies_count).wait_for(state="attached")
                vacancies_count = vacancies.count()
        except:
            pass
        for i in range(vacancies_count):
            with step("got the name of the city"):
                block = vacancies.nth(i)
                city_locator_str = vacancies_page.city_name_in_vacancies.format_locator.format(city_name=city_name)
                city_locator = block.locator(city_locator_str)
                city = city_locator.text_content()
                cityes.append(city)
                print(f"Vacancy {i+1}, city name: {city}")
        with step("Vacancies and Cityes count check"):
            assert vacancies_count == len(cityes)
            if vacancies_count == len(cityes):
                print(f"Vacancies count: {vacancies_count} equal to Сityes count: {len(cityes)}")
            else:
                print(f"Vacancies count: {vacancies_count} does not equal to Сityes count: {len(cityes)}")

    @step("filter without vacancies check")
    def filter_without_vacancies_check(self, city_name, directions):
        with step("open vacancies page"):
            with self.page.context.expect_page() as new_page_info:
                self.main_page.vacancies_page_click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        vacancies_page = VacanciesPage(new_page)
        with step("filter city chose"):
            vacancies_page.city_filter_click(city_name)
        with step("filter directions chose"):
            vacancies_page.directions_filter_click(directions)
            vacancies_page.activated_filter.format(filter_name=directions).wait_for(state="visible")
        vacancies_page.clear_all_filters_button.scroll_into_view_if_needed()
        vacancies_page.vacancies_block.wait_for(state="hidden", timeout=4000)
        with step("vacancies found and clear filter button check"):
            print(f"\nCity:{city_name}\n"
                  f"Directions:{directions}"
                  )
            if vacancies_page.no_vacancies_found_message.is_visible(timeout=2000):
                print("No vacancies found")
                if vacancies_page.clear_all_filters_button.is_enabled(timeout=2000):
                    print("Clear all filters button enabled")
                else:
                    raise AssertionError("Clear all filters button disabled")
            else:
                raise AssertionError("Vacancies found")

    @step("incorrect product name search check")
    def incorrect_product_name_search_check(self):
        self.main_page.incorrect_product_name_message.wait_for(state="visible", timeout=2000)
        if self.main_page.incorrect_product_name_message.is_visible(timeout=2000):
            print("Incorrect product name message is visible")
        else:
            raise AssertionError("Product found")

    @step("search with special symbol field check")
    def search_with_special_symbol_field_check(self, special_symbol_name):
        self.main_page.search_results_product.wait_for(state="visible", timeout=2000)
        product_name_title = self.main_page.search_results_product.get_locator
        search_results_count = product_name_title.count()
        print(f"Product name: '{special_symbol_name}'")
        for i in range(search_results_count):
            with step(f"Product inspection {i}"):
                product_block = product_name_title.nth(i)
                product_name = product_block.text_content()

                product_name_lower = product_name.lower()
                special_symbol_name_clean = re.sub(r"[^a-zа-яіїєґ\s]", "", special_symbol_name, flags=re.IGNORECASE).lower().strip()
                print(
                    f"Product inspection {i+1}, product name: '{product_name}'"
                )
                if special_symbol_name_clean not in product_name_lower:
                    raise AssertionError(
                        f"Error: name: '{product_name}' dont have this part: '{special_symbol_name}'"
                    )
        print("All products valid")

    @step("add email invalid format check")
    def add_email_invalid_format_check(self):
        if self.settings_page.input_error_message.is_visible(timeout=2000):
            print("Email error message is visible")
        else:
            raise AssertionError("Email error message not visible")

    @step("navigate to subcategory check")
    def navigate_to_subcategory_check(self, subcategory_name):
        self.egg_and_milk_category_page.subcategory_name_title.format(category_name=subcategory_name).wait_for(state="visible")
        product_name_title_locator = self.egg_and_milk_category_page.product_name_title.get_locator
        product_name_title_count = product_name_title_locator.count()
        subcategory = subcategory_name.lower()
        for i in range(product_name_title_count):
            product_block = product_name_title_locator.nth(i)
            product_name = product_block.text_content().lower()
            print(f"Product name: '{product_name}'")
            words = product_name.split()
            if not any(subcategory in word for word in words):
                raise AssertionError(
                    f"Product: '{product_name}' doesn't contain keyword '{subcategory_name}'"
                )
        print(f"All products fit the subcategory: '{subcategory_name}'")

    @step("product quantity display check")
    def product_quantity_display_check(self):
        self.bbq_page.product_quantity.wait_for(state="visible", timeout=2000) #####
        if self.bbq_page.product_quantity.is_visible(timeout=2000):
            print("Product quantity is visible")
        else:
            raise AssertionError("Product quantity not visible")

    @step("sort by price (high to low) check")
    def sort_by_price_high_check(self):
        self.wrapper.wait_for_timeout(1000)
        price_blocks = self.bbq_page.price_block.get_locator
        price_blocks_count = price_blocks.count()
        previous_price = None
        for i in range(price_blocks_count):
            block = price_blocks.nth(i)
            start_text = block.locator(self.bbq_page.start_product_price.locator).text_content()
            start_val = self._parse_price(start_text)

            end_price_locator = block.locator(self.bbq_page.end_product_price.locator)
            end_val = None
            if end_price_locator.count() > 0:
                end_text = end_price_locator.text_content()
                end_val = self._parse_price(end_text)

            if start_val == -1 or (end_val is not None and end_val == -1):
                print(f"Warning: price not recognized for product {i}, skip.")
                continue

            if end_val is None:
                extreme_price = start_val
            else:
                extreme_price = max(start_val, end_val)

            print(
                f"Product {i}: start price = {start_val}, "
                f"end price = {end_val if end_val is not None else 'absent'}"
            )

            if previous_price is not None and extreme_price > previous_price:
                raise AssertionError(
                    f"Product {i} has price {extreme_price}, "
                    f"which is greater than previous product price {previous_price}"
                )

            previous_price = extreme_price
        print("All products are correctly sorted from high to low.")

    @step("add postal machine address check")
    def add_postal_machine_address_check(self):
        address_from_site = self.address_page.added_address.get_text()
        if Variables.POSTAL_MACHINE_CITY and Variables.POSTAL_MACHINE_ADDRESS in address_from_site:
            print(f"Addresses match: site address {address_from_site};\n"
                  f"Input address {Variables.POSTAL_MACHINE_ADDRESS}, {Variables.POSTAL_MACHINE_CITY}"
                  )
        else:
            raise AssertionError(f"Addresses sre different: {address_from_site}, {Variables.POSTAL_MACHINE_ADDRESS, Variables.POSTAL_MACHINE_CITY}")
