import requests
from pytest_voluptuous import S
from schemas.reqres import response_list_users

BASE_URL = "https://reqres.in"

def test_response_list_users():
    headers = {"x-api-key": "reqres-free-v1"}
    response = requests.get(url=f"{BASE_URL}/api/users", headers=headers)

    assert S(response_list_users) == response.json()