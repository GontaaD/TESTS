import allure
from zakaz_ua.pages.base_page import BasePage
from page_wrapper import PageWrapper as Pgw

class BaseElement(BasePage):
    def __init__(self, page):
        self.wrapper = Pgw(page)
        self._formatted_locator = None
        super().__init__(page)

    @property
    def locator(self):
        if self._formatted_locator:
            return self._formatted_locator
        raise NotImplementedError("The descendant class must define locator property")

    @property
    def format_locator(self):
        raise NotImplementedError("The descendant class must define raw_locator property")

    def format(self, *args, **kwargs):
        with allure.step(f"Format locator with args: {args}, kwargs: {kwargs}"):
            self._formatted_locator = self.format_locator.format(*args, **kwargs)
            return self

    def click(self):
        with allure.step(f"Click {self.locator}"):
            try:
                self.wrapper.click(self.locator)
            except TimeoutError:
                AssertionError (f"Failed to click {self.locator}")

    def fill(self, value: str):
        with allure.step(f"Fill {self.locator} with {value}"):
            try:
                self.wrapper.fill(self.locator, value)
            except TimeoutError:
                AssertionError(f"Failed to fill {self.locator} with {value}")

    def clear(self):
        with allure.step(f"Clear {self.locator}"):
            try:
                self.wrapper.fill(self.locator, "")
            except TimeoutError:
                AssertionError(f"Failed to clear {self.locator}")

    def get_text(self, locator: str = None):
        with allure.step(f"Get {self.locator} text"):
            try:
                return self.wrapper.get_text(locator or self.locator)
            except TimeoutError:
                AssertionError(f"Failed to get {self.locator} text")

    @property
    def is_visible(self):
        with allure.step(f"Is {self.locator} visible"):
            try:
                return self.wrapper.is_visible(self.locator)
            except TimeoutError:
                return False

    def type(self, value: str, delay: float = 0):
        with allure.step(f"Type {self.locator} with {value}"):
            try:
                self.wrapper.type(self.locator, value, delay=delay)
            except TimeoutError:
                AssertionError(f"Failed to type {self.locator} with {value}")

    @property
    def input_value(self):
        with allure.step(f"{self.locator} Input value"):
            try:
                return self.wrapper.input_value(self.locator)
            except TimeoutError:
                AssertionError(f"Failed {self.locator} Input value")

    @property
    def get_locator(self):
        with allure.step(f"Get {self.locator} locator"):
            try:
                return self.page.locator(self.locator)
            except TimeoutError:
                AssertionError(f"Failed to get {self.locator} locator")

    def count(self):
        with allure.step(f"Count elements by locator: {self.locator}"):
            try:
                return self.get_locator.count()
            except TimeoutError:
                AssertionError(f"Failed to count elements for {self.locator}")

    def scroll_into_view_if_needed(self):
        with allure.step(f"Scroll into view element by locator: {self.locator}"):
            try:
                self.wrapper.scroll_into_view_if_needed(self.locator)
            except TimeoutError:
                AssertionError(f"Failed to scroll element {self.locator} into view")