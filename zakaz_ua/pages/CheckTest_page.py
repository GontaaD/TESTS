import allure
from zakaz_ua.pages.list_page import ListPageLocators
from zakaz_ua.pages.BBQ_category_page import BBQCategoryPageLocators
from zakaz_ua.pages.base_page import BasePage
import re

class CheckTestPage(BasePage):
        # filter check
    @allure.step("check all price in range")
    def check_all_prices_in_range(self, enter_min_price, enter_max_price):
        price_blocks = self.page.locator(BBQCategoryPageLocators.PRICE_BLOCK)
        price_blocks_count = price_blocks.count()

        for i in range(price_blocks_count):
            block = price_blocks.nth(i)

            start_text = block.locator(BBQCategoryPageLocators.START_PRODUCT_PRICE).text_content()
            start_val = self._parse_price(start_text)

            end_price_locator = block.locator(BBQCategoryPageLocators.END_PRODUCT_PRICE)
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
                )

    @allure.step("price adjustment method")
    def _parse_price(self, text):
        cleaned = text.strip().lstrip("-").strip()
        cleaned = re.sub(r"[^\d.,]", "", cleaned)
        cleaned = cleaned.replace(",", ".")
        try:
            return float(cleaned)
        except ValueError:
            return -1

        # rename check
    @allure.step("check lists names")
    def rename_check(self, new_list_name, old_list_name):
        print(f"Name check: new name = '{new_list_name}', old name = '{old_list_name}'")
        assert new_list_name != old_list_name, (
            f"Error: the names are the same! new name = '{new_list_name}', old name = '{old_list_name}'"
        )

        #create new list check
    @allure.step("check create new list")
    def create_new_list_test(self, list_name):
        basepage = BasePage(self.page)
        replace_list_name_locator = ListPageLocators.CREATED_NEW_LIST.format(list_name=list_name)
        created_list_locator = self.page.locator(replace_list_name_locator)
        self.page.wait_for_timeout(500)
        basepage.is_visible(ListPageLocators.CREATED_NEW_LIST)
        list_count = created_list_locator.count()
        print(f"Object count:'{created_list_locator}' '{list_count}'")
        assert list_count != 0, (f"Object count:'{created_list_locator}' '{list_count}'")

        #delete lict check
    @allure.step("check delete list")
    def delete_list_check(self, list_name):
        basepage = BasePage(self.page)
        replace_list_name_locator = ListPageLocators.CREATED_NEW_LIST.format(list_name=list_name)
        created_list_locator = self.page.locator(replace_list_name_locator)
        self.page.wait_for_timeout(500)
        basepage.is_visible(ListPageLocators.CREATED_NEW_LIST)
        list_count = created_list_locator.count()
        print(f"Object count:'{created_list_locator}' '{list_count}'")
        assert list_count == 0, (f"Object count:'{created_list_locator}' '{list_count}'")

        #like test check
    @allure.step("check like")
    def like_check (self, productTitle1, productTitle2):
        print(f"Name check: '{productTitle1}', '{productTitle2}'")
        assert productTitle1 == productTitle2, (
            f"Error: the name are different: '{productTitle1}', '{productTitle2}'"
        )

        #change adding products to list check
    @allure.step("check change adding products")
    def change_product_check (self, productTitle1, productTitle2):
        print(f"Name check: '{productTitle1}', '{productTitle2}'")
        assert productTitle1 == productTitle2, (
            f"Error: the name are different: '{productTitle1}', '{productTitle2}'"
        )