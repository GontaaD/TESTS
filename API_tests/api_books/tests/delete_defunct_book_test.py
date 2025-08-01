import pytest
from allure import step

@pytest.mark.api
@pytest.mark.api_books
@step("api_test_delete_defunct_book_start")
def test_delete_defunct_book(api_wrapper, books):
    resp = api_wrapper.get_user()
    if len(resp["books"]) > 0:
        api_wrapper.delete_book(books[0])
    api_wrapper.raise_for_status = False
    resp = api_wrapper.delete_book(books[0])
    assert resp.status_code in (400, 404), \
        "Failed test, status code are different"
    print(f"status code: {resp.status_code}"
          "\nCannot delete a non-existent book"
          )