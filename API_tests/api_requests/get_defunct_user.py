import requests

headers = {
    "x-api-key": "reqres-free-v1"
}
response = requests.get("https://reqres.in/api/users/23", headers=headers)
assert response.status_code == 404, f"status code not 404, status code = {response.status_code}"
assert response.json() == {}, f"the answer is not empty: {response.json()}"
print(response.status_code, response.json())