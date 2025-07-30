import pytest
from allure import step

@pytest.mark.api
@pytest.mark.api_contacts
@step("test_replace_multiple_attributes_start")
def test_replace_multiple_attributes(api_wrapper):
    apdated_fields = {
        "city": "Київ",
        "firstName": "Максим",
        "birthdate": "2000-10-10",
    }
    resp = api_wrapper.add_contact(2)
    api_wrapper.replace_attribute(resp[0], **apdated_fields)
    resp = api_wrapper.get_contacts()
    assert len(resp) == 2
    for field, value in apdated_fields.items():
        assert resp[0][field] == value
        assert resp[1][field] != value
    api_wrapper.delete_all_contacts()