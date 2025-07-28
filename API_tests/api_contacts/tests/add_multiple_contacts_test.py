import pytest
from allure import step

@pytest.mark.api_contacts
@step("test_add_multiple_contacts_start")
def test_add_multiple_contacts(api_wrapper):
    resp = api_wrapper.add_contact(3)
    assert len(resp) == 3, f"Failed test, contact count: {len(resp)}, not 3"
    print(f"contacts count: {len(resp)}:",
          f"\n{resp[0]}",
          f"\n{resp[1]}",
          f"\n{resp[2]}"
          )
    api_wrapper.delete_all_contacts()