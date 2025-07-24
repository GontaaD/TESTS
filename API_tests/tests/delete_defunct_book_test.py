import pytest
from allure import step

@pytest.mark.api
@step("api_test_delete_defunct_book_start")
def test_delete_defunct_book(api_wrapper, books):
    resp = api_wrapper.get_user()
    if len(resp["books"]) > 0:
        api_wrapper.delete_book(books[0])
    api_wrapper.raise_for_status = False
    resp = api_wrapper.delete_book(books[0])
    assert resp.status_code in (400, 404)