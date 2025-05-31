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

    # Клікнути на кнопку "Бічна панель"
    page.wait_for_selector('button.header__button')
    page.click('button.header__button')

    page.wait_for_timeout(500)
    #Клікнути на кнопку "Увійти"
    page.wait_for_selector('button.button.button--navy.button--small.user-login__button')
    page.click('button.button.button--navy.button--small.user-login__button')

    page.wait_for_timeout(500)
    #Закрити бічне меню
    page.click('button.close.ms-2')

    page.wait_for_timeout(500)
    #Введення номеру
#
    phone_input = page.wait_for_selector('input.LeAKF')
    phone_input.click()
    phone_input.type('997952094')
#
    page.wait_for_timeout(1000)

    # Натиснути кнопку "Отримати код" (перевірити селектор)
    page.click('button._00LHV.fsoe1.NQrpD.fAKin')

    # Можна додати паузу для ручного введення коду (опціонально)
    page.wait_for_timeout(20000)  # пауза

    # Після введення коду перевірити, що увійшли (наприклад, по появі іконки профілю)
    page.wait_for_selector('p.user-personal-info__name')
    profile_name = page.inner_text('p.user-personal-info__name')
    assert profile_name == "Денис Гонта"

    page.close()
