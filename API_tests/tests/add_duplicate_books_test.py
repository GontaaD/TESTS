import pytest
from allure import step

@pytest.mark.api
@step("api_test_add_duplicate_books_start")
def test_add_duplicate_books(api_wrapper, books):
    api_wrapper.add_books(books[0])
    api_wrapper.raise_for_status = False
    resp = api_wrapper.add_books(books[0])
    assert resp.status_code in (400, 404)