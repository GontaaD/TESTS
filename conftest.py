import os
import shutil

def pytest_sessionstart(session):
    allure_dir = session.config.getoption("--alluredir")
    if allure_dir and os.path.exists(allure_dir):
        print(f"Deleting Allure results folder: {allure_dir}")
        shutil.rmtree(allure_dir)
    if allure_dir:
        os.makedirs(allure_dir, exist_ok=True)
        print(f"Creating Allure results folder: {allure_dir}")