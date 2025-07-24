import requests

headers = {
    "x-api-key": "reqres-free-v1"
}

response = requests.get("https://reqres.in/api/users?page=1", headers=headers)
json_data = response.json()
assert response.status_code == 200
assert json_data["total_pages"] >= 2
data = json_data.get("data")
per_page = json_data.get("per_page")
assert len(data) == per_page
print(response.status_code, json_data["total_pages"], len(data), per_page)