import pytest
from allure import step

@pytest.mark.api
@step("api_test_add_books_start")
def test_add_books(api_wrapper, books):
    api_wrapper.add_books(books[0], books[1])
    resp = api_wrapper.get_user()
    assert len(resp["books"]) == 2, f"books count {len(resp['books'])}, not 2"
    assert resp["books"][0]["isbn"] == books[0]
    assert resp["books"][1]["isbn"] == books[1]