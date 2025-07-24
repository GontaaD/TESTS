from requests import Session
from allure import step

class ApiWrapper(object):
    def __init__(self):
        self.host = "https://demoqa.com/"
        self.user_name = None
        self.password = None
        self.session = Session()
        self.user_id = None
        self.raise_for_status = True

    @step("request")
    def request(self, method, url, **kwargs):
        response = self.session.request(method, f"{self.host}{url}", **kwargs)
        if self.raise_for_status:
            response.raise_for_status()
        return response

    @step("get_books")
    def get_books(self) -> dict:
        return self.request("GET", "BookStore/v1/Books").json()

    @step("create_user")
    def create_user(self):
        payload = {
          "userName": self.user_name,
          "password": self.password
        }
        return self.request("POST", "Account/v1/User", json=payload)

    @step("generate_token")
    def generate_token(self):
        payload = {
          "userName": self.user_name,
          "password": self.password
        }
        return self.request("POST", "Account/v1/GenerateToken", json=payload)

    @step("user_login")
    def user_login(self) -> dict:
        payload = {
          "userName": self.user_name,
          "password": self.password
        }
        return self.request("POST", "Account/v1/Login", json=payload).json()

    @step("get_user")
    def get_user(self) -> dict:
        return self.request("GET", f"Account/v1/User/{self.user_id}").json()

    @step("add_books")
    def add_books(self, *isbns):
        payload = {
          "userId": self.user_id,
          "collectionOfIsbns": [{"isbn": books} for books in isbns]
        }
        return self.request("POST", "BookStore/v1/Books", json=payload)

    @step("delete_book")
    def delete_book(self, book):
        payload = {
          "isbn": book,
          "userId": self.user_id
        }
        return self.request("DELETE", "BookStore/v1/Book", json=payload)

    @step("replace_books")
    def replace_books(self, book1, book2):
        payload = {
          "userId": self.user_id,
          "isbn": book2
        }
        return self.request("PUT", f"BookStore/v1/Books/{book1}", json=payload)

    @step("delete_books")
    def delete_books(self):
        params = {
            "UserId": self.user_id,
        }
        return self.request("DELETE", "BookStore/v1/Books", params=params)

    @step("delete_user")
    def delete_user(self):
        return self.request("DELETE", f"Account/v1/User/{self.user_id}")

    @step("prepare_user")
    def prepare_user(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.create_user()
        self.generate_token()
        resp = self.user_login()
        self.user_id = resp["userId"]
        self.session.headers["Authorization"] = f"Bearer {resp['token']}"
