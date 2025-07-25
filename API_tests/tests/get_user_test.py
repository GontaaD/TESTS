import pytest
from allure import step

@pytest.mark.api
@step("api_test_get_user_start")
def test_get_user(api_wrapper, books):
    resp = api_wrapper.get_user()
    assert resp["username"] == api_wrapper.user_name, \
        "Failed test, wrong username"
    assert resp["userId"] == api_wrapper.user_id, \
        f"Failed test, wrong user id"
    assert len(resp["books"]) == 0, \
        "Failed test, books are present"
    print("user data received and correct")