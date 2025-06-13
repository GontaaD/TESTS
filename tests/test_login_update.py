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

    #Закрити бічне меню
    #page.click('button.close.ms-2')

    page.wait_for_timeout(2000)
    #Введення номеру
    # Дочекайся завантаження сторінки
    page.wait_for_load_state("domcontentloaded")

    # Виведи всі фрейми — це ключовий дебаг
    #for f in page.frames:
        #print("FRAME:", f.name, f.url)

    # Знайди фрейм, де є поле
    frame = None
    for f in page.frames:
        if f.locator('//input[@data-qaid="phone"]').count() > 0:
            frame = f
            break

    if frame:
        frame.fill('//input[@data-qaid="phone"]', '997952094')

        button = frame.locator('button._00LHV.fsoe1.NQrpD.fAKin')
        button.wait_for(state='visible')
        button.click()
    else:
        raise Exception("Фрейм із полем не знайдено!")

    # Можна додати паузу для ручного введення коду (опціонально)
    page.wait_for_timeout(10000)  # пауза

    # Після введення коду перевірити, що увійшли (наприклад, по появі іконки профілю)
    page.wait_for_selector('p.user-personal-info__name')
    profile_name = page.inner_text('p.user-personal-info__name')
    assert profile_name == "Денис Гонта"

    page.close()