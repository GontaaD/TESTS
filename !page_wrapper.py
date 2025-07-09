from playwright.sync_api import Page, ElementHandle, TimeoutError as PlaywrightTimeoutError
import pytest
import platform


#class PageWrapper:

    #def __init__(self, page: Page):
    #   self.page = page
    #
    # def goto(self, url: str):
    #     self.page.goto(url)
    #
    # def current_url(self) -> str:
    #     # return self.page.url
    #     return self.page.evaluate("window.location.href")
    #
    # """
    # def wait_for_url(self, url) -> str:
    #     return self.page.wait_for_url(url=url)
    # """
    #
    # def wait_for_load(self):
    #     try:
    #         self.page.wait_for_load_state()
    #     except PlaywrightTimeoutError:
    #         pytest.fail(f"Load state has not been reached")
    #
    # def set_default_timeout(self, sec):
    #     self.page.set_default_timeout(sec)
    #
    # def fill_input(self, locator: str, value: str):
    #     self.get_element(locator).fill(value)
    #
    # def get_input_value(self, locator: str) -> str:
    #     return self.page.input_value(locator)
    #
    # def click(self, locator: str, force=False):
    #     self.get_element(locator).click(force=force)
    #
    # def dblclick(self, locator: str):
    #     self.get_element(locator).dblclick()
    #
    # def right_click(self, locator: str):
    #     self.get_element(locator).click(button='right')
    #
    # def shift_and_click(self, locator: str):
    #     self.get_element(locator).click(modifiers=['Shift'])
    #
    # def get_title(self) -> str:
    #     return self.page.title()
    #
    # def get_text(self, locator: str):
    #     return self.get_element(locator).inner_text()
    #
    # def get_text_content(self, locator: str):
    #     return self.get_element(locator).text_content()
    #
    # def clear_text(self, locator: str):
    #     return self.get_element(locator).clear()
    #
    # def get(self):
    #     return self.get()
    #
    # def _build_locator_attributes(self, **kwargs) -> str:
    #     attributes = ""
    #     for attr, value in kwargs.items():
    #         attributes += f'[{attr}="{value}"]'
    #     return attributes
    #
    # def get_by_role(self, role, value):
    #     return self.page.get_by_role(role, name=value)
    #
    # def get_element(self, locator: str):
    #     str_cat = locator[:locator.find('=')]
    #     str_value = locator[locator.find('=') + 1:]
    #     if str_cat == "text":
    #         return self.page.get_by_text(str_value)
    #     elif str_cat == "label":
    #         return self.page.get_by_label(str_value)
    #     elif str_cat == "placeholder":
    #         return self.page.get_by_placeholder(str_value)
    #     else:
    #         return self.page.locator(str_value)
    #
    # """
    # for text: get_element("text=Welcome, John!")
    # for label: get_element("label=Username")
    # for placeholder: get_element("placeholder=name@example.com")
    # for xpath: get_element("xpath=//*[@data-cy='login-dialog__register-link']")
    #
    # """
    #
    # def get_box(self, locator: str):
    #     return self.get_element(locator).bounding_box()
    #
    # def get_attribute(self, locator: str, attribute_name: str):
    #     return self.get_element(locator).get_attribute(attribute_name)
    #
    # def press_keyboard(self, key_name: str):
    #     if platform.system() == 'Darwin' and key_name == "Control":  # macOS
    #         key_name = "Meta"
    #     self.page.keyboard.press(key_name)
    #
    # def down_keyboard(self, key_name: str):
    #     if platform.system() == 'Darwin' and key_name == "Control":  # macOS
    #         key_name = "Meta"
    #     self.page.keyboard.down(key_name)
    #
    # def up_keyboard(self, key_name: str):
    #     if platform.system() == 'Darwin' and key_name == "Control":  # macOS
    #         key_name = "Meta"
    #     self.page.keyboard.up(key_name)
    #
    # def mouse_click(self, x, y):
    #     self.page.mouse.click(x, y)
    #
    # def mouse_hover(self, locator):
    #     self.get_element(locator).hover()
    #
    # """
    # def get_all_elements(self, locator: str):
    #     dropdown = self.get_element(locator)
    #     options = dropdown.get_by_role('mat-option').all()
    #     return options
    # """
    #
    # def get_clipboard_value(self):
    #     return self.page.evaluate('() => navigator.clipboard.readText()')
    #
    # def wait_for_element_visible(self, locator: str, msec):
    #     try:
    #         self.get_element(locator).wait_for(state="visible", timeout=msec)
    #     except PlaywrightTimeoutError:
    #         pytest.fail(f"Element '{locator}' does not visible after {msec} ms.")
    #
    # def wait_for_element_present(self, locator: str, msec):
    #     try:
    #         self.get_element(locator).wait_for(state="attached", timeout=msec)
    #     except PlaywrightTimeoutError:
    #         pytest.fail(f"Element '{locator}' does not present after {msec} ms")
    #
    # def wait_for_element_not_present(self, locator: str, msec):
    #     try:
    #         self.get_element(locator).wait_for(state="detached", timeout=msec)
    #     except PlaywrightTimeoutError:
    #         pytest.fail(f"Element '{locator}' does not present after {msec} ms")
    #
    # def execute_script(self, script: str):
    #     return self.page.evaluate(script)
    #
    # def refresh(self):
    #     self.page.reload()
    #
    # def frame_element(self, frame_locator: str, element_locator: str):
    #     self.page.frame_locator(frame_locator).locator(element_locator)
    #     return self.page.frame_locator(frame_locator).locator(element_locator)
    #
    # def wait_for_event(self, event, **kwargs):
    #     return self.page.wait_for_event(event, **kwargs)
    #
    # def evaluate_handle(self, expression, **kwargs):
    #     return self.page.evaluate_handle(expression, **kwargs)