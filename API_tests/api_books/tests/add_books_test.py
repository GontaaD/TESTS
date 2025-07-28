import pytest
from allure import step

@pytest.mark.api_books
@step("api_test_add_books_start")
def test_add_books(api_wrapper, books):
    api_wrapper.add_books(books[0], books[1])
    resp = api_wrapper.get_user()
    assert len(resp["books"]) == 2, \
        f"Failed test, books count {len(resp['books'])}, not 2"
    assert resp["books"][0]["isbn"] == books[0], \
        f"Failed test, book isbn are different: {resp['books'][0]['isbn']}, {books[0]}"
    assert resp["books"][1]["isbn"] == books[1], \
        f"Failed test, book isbn are different: {resp['books'][1]['isbn']}, {books[1]}"
    print(f"books: 'isbn': {books[0]}, 'isbn': {books[1]} are added")