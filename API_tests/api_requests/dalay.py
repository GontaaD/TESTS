import requests
import time

start = time.time()
response = requests.get("https://reqres.in/api/users?delay=3")
end = time.time()
elapsed = end - start
print(f"Time taken: {elapsed:.2f} seconds")