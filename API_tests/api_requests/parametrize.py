import requests
import pytest

@pytest.mark.parametrize("param", [7, 8, 9, 10, 11, 12])
def test_parametrize(param):
    headers = {
        "x-api-key": "reqres-free-v1"
    }
    response = requests.get("https://reqres.in/api/users?page=2", headers=headers)
    data = response.json()["data"]
    id = [user["id"] for user in data]
    assert param in id
    print(id)
