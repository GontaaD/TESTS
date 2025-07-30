import pytest
import allure
from playwright.sync_api import sync_playwright

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_browser(self, request, get_cookies):
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=True)

            self.context = self.browser.new_context(
                permissions=["geolocation"],
                geolocation={"latitude": 50.7472, "longitude": 25.3254},
                locale="uk-UA",
            )
            if not request.node.get_closest_marker("login"):
                self.context.add_cookies(get_cookies)

            self.page = self.context.new_page()
            self.page.goto("https://zakaz.ua/uk/", wait_until="load")

            yield
            if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
                screenshot = self.page.screenshot()
                allure.attach(
                    screenshot,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            self.context.close()
            self.browser.close()

    @pytest.hookimpl(hookwrapper=True, tryfirst=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        rep = outcome.get_result()
        setattr(item, "rep_" + rep.when, rep)

