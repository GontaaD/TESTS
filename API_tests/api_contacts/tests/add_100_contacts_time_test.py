import time
import pytest
from allure import step

@pytest.mark.api
@pytest.mark.api_contacts
@step("test_add_100_contacts_time_start")
def test_add_100_contacts_time(api_wrapper):
    start = time.time()
    resp = api_wrapper.add_contact(100)
    end = time.time()
    assert len(resp) == 100
    api_wrapper.delete_all_contacts()
    duration = end - start
    print(f"{duration} seconds")
