import os
import shutil
import requests
import pytest
from helper.variables_page import Variables


def pytest_sessionstart(session):
    allure_dir = session.config.getoption("--alluredir")
    if allure_dir and os.path.exists(allure_dir):
        print(f"Deleting Allure results folder: {allure_dir}")
        shutil.rmtree(allure_dir)
    if allure_dir:
        os.makedirs(allure_dir, exist_ok=True)
        print(f"Creating Allure results folder: {allure_dir}")

@pytest.fixture(scope="session")
def get_cookies():
    url = "https://stores-api.zakaz.ua/user/login/"
    payload = {
        "login": Variables.user_data["login"],
        "password": Variables.user_data["password"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    session = requests.Session()
    response = session.post(url, json=payload, headers=headers)

    response.raise_for_status()

    cookies = []
    for cookie in session.cookies:
        cookies.append({
            "name": cookie.name,
            "value": cookie.value,
            "domain": cookie.domain if cookie.domain else "zakaz.ua",
            "path": cookie.path,
            "httpOnly": bool(cookie._rest.get("HttpOnly", False)),
            "secure": bool(cookie.secure),
            "sameSite": cookie._rest.get("SameSite", "Lax")
        })
    return cookies