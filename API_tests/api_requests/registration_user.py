import requests

headers = {
    "x-api-key": "reqres-free-v1"
}

payload = {
  "name": "Denis",
  "job": "QA"
}
response = requests.post("https://reqres.in/api/users", json=payload, headers=headers)
response.json = response.json()
assert response.status_code == 201, f"status code not 201, status code = {response.status_code}"
assert response.json.get("name") == "Denis" and response.json.get("job") == "QA"
assert 'id' in response.json and 'createdAt' in response.json
print(response.status_code, response.json)