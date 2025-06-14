import pytest
from playwright.sync_api import sync_playwright
import cart_paterns

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_add_product_to_cart(browser):
    page = browser.new_page()
    page.goto("https://rozetka.com.ua", wait_until="load")

    page.wait_for_selector(cart_paterns.SEARCH_INPUT)
    page.fill(cart_paterns.SEARCH_INPUT, "Ноутбук Apple MacBook Air 13 M1 8/256GB 2020 (MGN63) Space Gray")
    page.click(cart_paterns.SEARCH_BUTTON)

    page.wait_for_selector(cart_paterns.CART_ADD_ICON)
    product_name = page.locator(cart_paterns.SPAN_MACBOOK).first.text_content()
    page.click(cart_paterns.CART_ADD_ICON)

    page.wait_for_selector(cart_paterns.CART_BUTTON)
    page.click(cart_paterns.CART_BUTTON)

    cart_product = page.locator(cart_paterns.SPAN_MACBOOK).first.text_content()
    assert product_name.strip() in cart_product, "Товар не знайдено в кошику"

    page.close()


