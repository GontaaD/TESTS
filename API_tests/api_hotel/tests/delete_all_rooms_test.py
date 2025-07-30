import pytest
from allure import step

@pytest.mark.api
@pytest.mark.api_hotel
@step("api_test_delete_all_room")
def test_all_delete_room(api_wrapper):
    api_wrapper.create_room(3)
    api_wrapper.delete_all_rooms()
    resp = api_wrapper.get_rooms()
    assert len(resp) == 0