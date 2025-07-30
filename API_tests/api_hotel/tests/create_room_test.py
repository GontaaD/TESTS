import pytest
from allure import step

@pytest.mark.api
@pytest.mark.api_hotel
@step("api_test_create_room")
def test_create_room(api_wrapper):
    count = 3
    rooms = api_wrapper.get_rooms()
    api_wrapper.create_room(count)
    resp = api_wrapper.get_rooms()
    assert len(resp) == len(rooms)+count
