from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):
        self.page.wait_for_selector(locator)
        self.page.click(locator)

    def fill(self, locator):
        self.page.wait_for_selector(locator)
        self.page.fill(locator)

    def is_visible(self, locator):
        return self.page.is_visible(locator)

    def get_text(self, locator):
        self.page.wait_for_selector(locator)
        return self.page.locator(locator).text_content()

