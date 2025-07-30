import pytest
from allure import step

@pytest.mark.api
@pytest.mark.api_contacts
@step("test_replace_number_start")
def test_replace_number(api_wrapper):
    phone = "0990000000"
    resp = api_wrapper.add_contact()
    resp = api_wrapper.replace_attribute(resp[0], phone=phone)
    assert resp["phone"] == phone
    print(resp["phone"])
    api_wrapper.delete_all_contacts()