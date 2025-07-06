from zakaz_ua.pages.list_page import ListPageLocators
from zakaz_ua.pages.BBQ_category_page import BBQCategoryPageLocators
from zakaz_ua.pages.base_page import BasePage
import re

class CheckTestPage(BasePage):

        # filter check

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
                f"Перевірка товару {i}: стартова ціна = {start_val}, кінцева ціна = {end_val if end_val is not None else 'відсутня'}"
            )

            if start_val == -1 or (end_val is not None and end_val == -1):
                print(f"Попередження: ціна не розпізнана для товару {i}, пропускаємо.")
                continue

            if end_val is None:
                end_val = start_val

            min_price = min(start_val, end_val)
            max_price = max(start_val, end_val)

            if not (max_price >= enter_min_price and min_price <= enter_max_price):
                raise AssertionError(
                    f"Ціновий діапазон товару [{min_price} - {max_price}] "
                    f"не перекриває діапазон фільтра [{enter_min_price} - {enter_max_price}]"
                )

    def _parse_price(self, text):
        cleaned = text.strip().lstrip("-").strip()
        cleaned = re.sub(r"[^\d.,]", "", cleaned)
        cleaned = cleaned.replace(",", ".")
        try:
            return float(cleaned)
        except ValueError:
            return -1

        # rename check

    def rename_check(self, new_list_name, old_list_name):
        print(f"Перевірка назв: нова назва = '{new_list_name}', стара назва = '{old_list_name}'")
        assert new_list_name != old_list_name, (
            f"Помилка: назви списків збігаються! нова назва = '{new_list_name}', стара назва = '{old_list_name}'"
        )

        #create new list check

    def create_new_list_test(self, list_name):
        basepage = BasePage(self.page)
        replace_list_name_locator = ListPageLocators.CREATED_NEW_LIST.format(list_name=list_name)
        created_list_locator = self.page.locator(replace_list_name_locator)
        self.page.wait_for_timeout(500)
        basepage.is_visible(ListPageLocators.CREATED_NEW_LIST)
        list_count = created_list_locator.count()
        print(f"кількість обʼєктів:'{created_list_locator}' '{list_count}'")
        assert list_count != 0, (f"кількість обʼєктів:'{created_list_locator}' '{list_count}'")

        #delete lict check

    def delete_list_check(self, list_name):
        basepage = BasePage(self.page)
        replace_list_name_locator = ListPageLocators.CREATED_NEW_LIST.format(list_name=list_name)
        created_list_locator = self.page.locator(replace_list_name_locator)
        self.page.wait_for_timeout(500)
        basepage.is_visible(ListPageLocators.CREATED_NEW_LIST)
        list_count = created_list_locator.count()
        print(f"кількість обʼєктів:'{created_list_locator}' '{list_count}'")
        assert list_count == 0, (f"кількість обʼєктів:'{created_list_locator}' '{list_count}'")
