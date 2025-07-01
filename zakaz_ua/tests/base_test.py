import pytest
from playwright.sync_api import sync_playwright

class BaseTest:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=False)
            self.page = self.browser.new_page()
            yield
            self.browser.close()
