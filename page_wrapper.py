from playwright.sync_api import Page

class PageWrapper:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):
        self.page.click(locator)

    def fill(self, locator: str, value: str):
        self.page.fill(locator, value)

    def get_text(self, locator: str):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator: str):
        return self.page.is_visible(locator)

    def wait_for_timeout(self, ms: int):
        self.page.wait_for_timeout(ms)

    def type(self, locator: str, value: str, delay: float = 0):
        self.page.type(locator, value, delay=delay)

    def input_value(self, locator: str):
        return self.page.locator(locator).input_value()


