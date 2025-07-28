import pytest
from allure import step

@pytest.mark.api_contacts
@step("test_delete_all_contacts_start")
def test_delete_all_contacts(api_wrapper):
    api_wrapper.add_contact(5)
    api_wrapper.delete_all_contacts()
    resp_list = api_wrapper.get_contacts()
    assert resp_list == [], "Failed test, the contact is not deleted"