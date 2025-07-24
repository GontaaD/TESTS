import requests

headers = {
    "x-api-key": "reqres-free-v1"
}

payload = {
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}
response = requests.post("https://reqres.in/api/login", json=payload, headers=headers)
response.json = response.json()
assert response.status_code == 200, f"status code not 200, status code = {response.status_code}"
assert 'token' in response.json, f"token not in: {response.json()}"
print(response.status_code, response.json)