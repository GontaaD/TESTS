from zakaz_ua.locators.locators import BBQCategoryPageLocators
from zakaz_ua.pages.base_page import BasePage
import re

class BBQPage(BasePage):
    def click_heart_button(self):
        self.page.click(BBQCategoryPageLocators.HEART_BUTTON)

    def first_search_product_name(self):
        return self.get_text(BBQCategoryPageLocators.PRODUCT_TITLE)

    def open_navigator(self):
        self.page.hover(BBQCategoryPageLocators.ACCOUNT_NAVIGATOR)

    def click_heart_list_button(self):
        self.page.click(BBQCategoryPageLocators.HEART_LIST_BUTTON)

    def set_max_price(self, enter_max_price):
        self.page.fill(BBQCategoryPageLocators.MAX_PRICE_FILTER, str(enter_max_price))

    def set_min_price(self, enter_min_price):
        self.page.fill(BBQCategoryPageLocators.MIN_PRICE_FILTER, str(enter_min_price))

    def click_filter_apply_button(self):
        self.page.click(BBQCategoryPageLocators.FILTER_APPLY_BUTTON)
        self.page.wait_for_timeout(2000)

    def fill_price_filter(self, enter_min_price, enter_max_price):
        self.set_max_price(enter_max_price)
        self.set_min_price(enter_min_price)
        self.click_filter_apply_button()

    def check_all_prices_in_range(self, enter_min_price, enter_max_price):
        price_blocks = self.page.locator(BBQCategoryPageLocators.PRICE_BLOCK)
        price_blocks_count = price_blocks.count()

        for i in range(price_blocks_count):
            block = price_blocks.nth(i)

            # Витягуємо стартову ціну у межах блоку
            start_text = block.locator(BBQCategoryPageLocators.START_PRODUCT_PRICE).text_content()
            start_val = self._parse_price(start_text)

            # Витягуємо кінцеву ціну, якщо є
            end_price_locator = block.locator(BBQCategoryPageLocators.END_PRODUCT_PRICE)
            end_val = None
            if end_price_locator.count() > 0:
                end_text = end_price_locator.text_content()
                end_val = self._parse_price(end_text)

            print(
                f"Перевірка товару {i}: стартова ціна = {start_val}, кінцева ціна = {end_val if end_val is not None else 'відсутня'}"
            )

            # Пропускаємо, якщо парсинг не вдався
            if start_val == -1 or (end_val is not None and end_val == -1):
                print(f"Попередження: ціна не розпізнана для товару {i}, пропускаємо.")
                continue

            # Якщо кінцева ціна відсутня, беремо як рівну стартовій
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
            # Можна прибрати логування, якщо хочеш
            return -1
