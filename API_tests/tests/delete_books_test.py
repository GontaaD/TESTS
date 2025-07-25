import pytest
from allure import step

@pytest.mark.api
@step("api_test_delete_books_start")
def test_delete_books(api_wrapper, books):
    api_wrapper.add_books(books[0], books[1])
    api_wrapper.delete_books()
    resp = api_wrapper.get_user()
    assert len(resp["books"]) == 0, \
        "Failed test, the book is not deleted"
    print("All books deleted")