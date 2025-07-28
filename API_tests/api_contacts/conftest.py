from API_tests.api_contacts.api_wrapper import ApiWrapper
import pytest

EMAIL = "gontadenis2006@gmail.com"
PASSWORD = "gqk468Wp"

@pytest.fixture
def api_wrapper():
    api_wrapper = ApiWrapper()
    api_wrapper.prepare_user(EMAIL, PASSWORD)
    yield api_wrapper
