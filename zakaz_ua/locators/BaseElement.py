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

    def format(self, *args, **kwargs):
        self.clear_format()
        template = self.locator
        #template = super().locator if hasattr(super(), 'locator') else self.locator_template
        self._formatted_locator = template.format(*args, **kwargs)
        return self

    def clear_format(self):
        self._formatted_locator = None
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

    def get_text(self):
        with allure.step(f"Get {self.locator} text"):
            try:
                return self.wrapper.get_text(self.locator)
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
