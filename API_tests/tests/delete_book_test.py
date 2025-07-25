import pytest
from allure import step

@pytest.mark.api
@step("api_test_delete_book_start")
def test_delete_book(api_wrapper, books):
    api_wrapper.add_books(books[0], books[1])
    api_wrapper.delete_book(books[0])
    resp = api_wrapper.get_user()
    assert books[0] not in [books["isbn"] for books in resp["books"]], \
        "Failed test, the book is not deleted"
    print("Book deleted")