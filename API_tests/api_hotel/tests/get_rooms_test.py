import pytest
from allure import step

@pytest.mark.api
@pytest.mark.api_hotel
@step("api_test_get_rooms")
def test_get_rooms(api_wrapper):
    resp = api_wrapper.get_rooms()
    print(len(resp))
