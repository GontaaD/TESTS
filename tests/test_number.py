import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_login_by_phone(browser):
    page = browser.new_page()
    page.goto("https://rozetka.com.ua", wait_until="load")

    # Клікнути на кнопку "Увійти"
    page.wait_for_selector('button.header__button')
    page.click('button.header__button')

    page.wait_for_timeout(500)

    page.wait_for_selector('button.button.button--navy.button--small.user-login__button')
    page.click('button.button.button--navy.button--small.user-login__button')

    page.wait_for_timeout(500)

    page.click('button.close.ms-2')

    page.wait_for_timeout(500)

    # Чекати появи поля вводу телефону
    phone_input = page.locator('input.LeAKF')
    phone_input.wait_for(state="visible", timeout=15000)

    print("Видимість поля:", phone_input.is_visible())
    print("Активність поля:", phone_input.is_enabled())

    # Заповнюємо номер телефону
    page.fill('input.LeAKF', "501234567")

    # Коротка пауза, щоб UI "переварив" введене
    page.wait_for_timeout(500)

    # Перевірка, що номер реально введений
    value = phone_input.input_value()
    print("Введене значення:", value)

    assert value == "0501234567", "Номер телефону не введений"

    # Можна додати тут скріншот для візуальної перевірки (опційно)
    # page.screenshot(path="after_phone_input.png")
