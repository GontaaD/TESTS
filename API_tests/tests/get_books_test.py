import pytest
from allure import step

@pytest.mark.api
@step("api_test_get_books_start")
def test_get_books(api_wrapper, books):
    resp = api_wrapper.get_books()
    assert len(resp["books"]) == 8