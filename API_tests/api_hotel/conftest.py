from API_tests.api_hotel.api_wrapper import ApiWrapper
import pytest

USERNAME = "admin"
PASSWORD = "password"

@pytest.fixture
def api_wrapper():
    api_wrapper = ApiWrapper()
    api_wrapper.prepare_user(USERNAME, PASSWORD)
    yield api_wrapper