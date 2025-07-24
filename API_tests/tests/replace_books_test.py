import pytest
from allure import step

@pytest.mark.api
@step("api_test_replace_books_start")
def test_replace_books(api_wrapper, books):
    api_wrapper.add_books(books[0])
    api_wrapper.replace_books(books[0], books[1])
    resp = api_wrapper.get_user()
    assert resp["books"][0]["isbn"] == books[1]