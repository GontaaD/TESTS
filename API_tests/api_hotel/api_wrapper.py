from allure import step
from requests import Session

class ApiWrapper:
    def __init__(self):
        self.host = "https://automationintesting.online/api/"
        self.session = Session()
        self.username = None
        self.password = None
        self.raise_for_status = True

    @step("request")
    def request(self, method, url, **kwargs):
        full_url = f"{self.host}{url}"
        print(f"\n === Request ==="
              f"\n method: {method}"
              f"\n url: {full_url}"
              )
        if 'headers' in kwargs:
            print(f"headers: {kwargs['headers']}")
        if 'json' in kwargs:
            print(f"json: {kwargs['json']}")
        if 'params' in kwargs:
            print(f"params: {kwargs['params']}")
        response = self.session.request(method, full_url, **kwargs)
        print(f"\n === Response ==="
              f"\n status_code: {response.status_code}"
              f"\n text: {response.text}"
              f"\n --------------------------"
              )
        if self.raise_for_status:
            response.raise_for_status()
        return response

    def get_rooms(self):
        return self.request("GET", "room").json()["rooms"]

    def create_room(self, count=1):
        payload = {
          "roomName": "Test room",
          "type": "Double",
          "accessible": "true",
          "image": "https://www.example.com/room.jpg",
          "description": "Test room description",
          "features": ["WiFi", "TV"],
          "roomPrice": 100
        }
        results = []
        for _ in range(count):
            response = self.request("POST", "room", json=payload)
            results.append(response.json())
        return results

    def delete_room(self, room):
        return self.request("DELETE", f"room/{room['roomid']}")

    def delete_all_rooms(self):
        results = []
        for room in self.get_rooms():
            response = self.delete_room(room)
            results.append(response.status_code)
        return results

    def book_room(self, room, **kwargs):
        payload = {
            "bookingdates": {
                "checkin": "2025-07-16",
                "checkout": "2025-07-24"
            },
            "depositpaid": False,
            "email": "taras@gmail.com",
            "firstname": "tarasaaaaaaaaaa",
            "lastname": "shevchenkoa",
            "phone": "099123456711",
            "roomid": int(room["roomid"]),
        }
        if "bookingdates" in kwargs:
            payload["bookingdates"].update(kwargs.pop("bookingdates"))
        payload.update(kwargs)
        return self.request("POST", "booking", json=payload)

    def delete_booking(self, booking):
        params = {
            "bookingid": booking["bookingid"]
        }
        return self.request("DELETE", "booking", params=params)

    def login(self, username, password):
        payload = {
            "username": username,
            "password": password
        }
        return self.request("POST", "auth/login", json=payload).json()

    def prepare_user(self, username, password):
        self.username = username
        self.password = password
        response = self.login(username, password)
        self.session.cookies.set("token", response["token"])






