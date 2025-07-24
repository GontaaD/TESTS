import requests

response = requests.get("https://reqres.in/api/users/2")
data = response.json()
user = data.get("data")
assert user["first_name"] == "Janet"
print(response.status_code)
