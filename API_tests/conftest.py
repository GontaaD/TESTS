from API_tests.api_wrapper import ApiWrapper
import pytest

USER_NAME = "Denis"
PASSWORD = "Denis123#"

@pytest.fixture
def api_wrapper():
    api_wrapper = ApiWrapper()
    api_wrapper.prepare_user(USER_NAME, PASSWORD)
    yield api_wrapper
    api_wrapper.delete_user()

@pytest.fixture(scope="session")
def books():
    resp = ApiWrapper().get_books()
    return [i["isbn"] for i in resp["books"]]