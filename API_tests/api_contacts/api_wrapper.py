from requests import Session
from allure import step


class ApiWrapper:
    def __init__(self):
        self.host = "https://thinking-tester-contact-list.herokuapp.com/"
        self.session = Session()
        self.email = None
        self.password = None
        self.payload = {
            "birthdate": "1999-01-01",
            "city": "Луцьк",
            "country": "Україна",
            "email": "taras@gmail.com",
            "firstName": "Тарас",
            "lastName": "Шевченко",
            "phone": "0991234567",
            "postalCode": "43010",
            "stateProvince": "Волинська область",
            "street1": "вул.Ковельська "
        }

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
        return response

    @step("login")
    def login(self) -> dict:
        payload = {
            "email": self.email,
            "password": self.password
        }
        return self.request("POST", "users/login", json=payload).json()

    @step("add_contact")
    def add_contact(self, count=1):
        results = []
        for _ in range(count):
            response = self.request("POST", "contacts", json=self.payload)
            results.append(response.json())
        return results

    @step("get_contacts")
    def get_contacts(self):
        return self.request("GET", "contacts").json()

    @step("replace_attribute")
    def replace_attribute(self, contact, **kwargs):
        for key, value in kwargs.items():
            contact[key] = value
        return self.request("PUT", f"contacts/{contact['_id']}", json=contact).json()

    @step("delete_contact")
    def delete_contact(self, contact):
        return self.request("DELETE", f"contacts/{contact['_id']}")

    @step("delete_all_contacts")
    def delete_all_contacts(self):
        results = []
        contacts = self.get_contacts()
        for contact in contacts:
            response = self.delete_contact(contact)
            results.append(response.status_code)
        return results

    @step("prepare_user")
    def prepare_user(self, email, password):
        self.email = email
        self.password = password
        response = self.login()
        self.session.headers["Authorization"] = f"Bearer {response['token']}"

