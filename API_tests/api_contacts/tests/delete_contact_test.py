import pytest
from allure import step

@pytest.mark.api_contacts
@step("test_delete_contact_start")
def test_delete_contact(api_wrapper):
    resp = api_wrapper.add_contact(2)
    api_wrapper.delete_contact(resp[1])
    resp_list = api_wrapper.get_contacts()
    assert resp[1] not in resp_list, "Failed test, the contact is not deleted"
    api_wrapper.delete_all_contacts()