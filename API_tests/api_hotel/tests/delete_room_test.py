import pytest
from allure import step

@pytest.mark.api
@pytest.mark.api_hotel
@step("api_test_delete_room")
def test_delete_room(api_wrapper):
    api_wrapper.create_room(2)
    resp = api_wrapper.get_rooms()
    print(resp)
    api_wrapper.delete_room(resp[0])
    assert resp[0] not in api_wrapper.get_rooms()
