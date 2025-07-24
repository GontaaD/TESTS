import requests

response = requests.get("https://reqres.in/api/users?page=2")
data = response.json()["data"]
for user in data:
    full_name = f"{user['first_name']} {user['last_name']}"
    print(full_name)
print(response.status_code)