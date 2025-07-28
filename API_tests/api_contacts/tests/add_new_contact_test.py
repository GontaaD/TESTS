import pytest
from allure import step

@pytest.mark.api_contacts
@step("test_add_new_contact_start")
def test_add_new_contact(api_wrapper):
    resp = api_wrapper.add_contact()
    assert len(resp) == 1, \
    f"Failed test, contact count: {len(resp)}, not 1"
    print(f"contacts count: {len(resp)}")
    api_wrapper.delete_all_contacts()
