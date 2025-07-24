import requests

headers = {
    "x-api-key": "reqres-free-v1"
}

payload = {
  "email": "eve.holt@reqres.in"
}
response = requests.post("https://reqres.in/api/login", json=payload, headers=headers)
response.json = response.json()
assert response.status_code == 400, f"status code not 400, status code = {response.status_code}"
assert "error" in response.json
print(response.status_code, response.json)