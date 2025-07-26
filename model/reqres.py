from base_session import BaseSession
from config import Server


class User:
    def __init__(self, **kwargs):
        json_ = kwargs.pop("json", {})
        self._name = kwargs.pop("name", None)
        self._job = kwargs.pop("job", None)
        self._json = json_ if json_ else {
            "name": self._name,
            "job": self._job
        }

    @property
    def name(self):
        return self._json["name"]

    @property
    def job(self):
        return self._json["job"]

    @property
    def json(self):
        return self._json

class ResponseUser:
    def __init__(self, **kwargs):
        json_ = kwargs.pop("json", {})
        self._id = kwargs.pop("id", 2)
        self._email = kwargs.pop("email", "janet.weaver@reqres.in")
        self._first_name = kwargs.pop("first_name", "Janet")
        self._last_name = kwargs.pop("last_name", "Weaver")
        self._avatar = kwargs.pop("avatar", "https://reqres.in/img/faces/2-image.jpg")
        self._json = json_ if json_ else {
            "id": self._id,
            "email": self._email,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "avatar": self._avatar
        }

    @property
    def json(self):
        return self._json

class ResponseGetListUsers:
    def __init__(self, **kwargs):
        json_ = kwargs.pop("json", {})

        self._json = json_ if json_ else {
            "page": 2,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": []
        }

    def add_user(self, user: ResponseUser):
        self._json["data"].append(user)

        return self

    @property
    def json(self):
        return self._json

class Support:
    def __init__(self, **kwargs):
        self._url = kwargs.pop("url", "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral")
        self._text = kwargs.pop("text", "Tired of writing endless social media content? Let Content Caddy generate it for you.")
        self._json = {
            "url": self._url,
            "text": self._text
        }

    @property
    def url(self):
        return self._json["url"]

    @property
    def text(self):
        return self._json["url"]

    @property
    def json(self):
        return self._json


class ResponseGetSingleUser:
    def __init__(self, **kwargs):
        response = kwargs.pop("response", None)
        json_ = kwargs.pop("json", response.json() if response else None)
        self._data = kwargs.pop("data", ResponseUser().json)
        self._json = json_ if json_ else {
            "data": self._data,
            "support": {
                "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
                "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
            }
        }

    @property
    def json(self):
        return self._json

    @property
    def support_url(self):
        return self._json["support"]["url"]

    @property
    def support_text(self):
        return self._json["support"]["text"]

class Reqres:
    def __init__(self, env):
        self.session = BaseSession(base_url=Server(env).reqres)

    def get_user(self, user_id: int):
        return ResponseGetSingleUser(response=self.session.get(f"/api/users/{user_id}"))