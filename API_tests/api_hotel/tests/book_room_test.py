import pytest
from allure import step

@pytest.mark.api
@pytest.mark.api_hotel
@step("api_test_book_room")
def test_book_room(api_wrapper):
    api_wrapper.delete_all_rooms()
    payload = {"bookingdates": {
                "checkin": "2025-07-17",
                "checkout": "2025-07-25"
            }}
    api_wrapper.create_room()
    resp = api_wrapper.get_rooms()
    api_wrapper.book_room(resp[0], **payload)

