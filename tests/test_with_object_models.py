from model.reqres import ResponseGetSingleUser, ResponseUser, Reqres


def test_get_user(reqresin):
    expected_response_get_user = ResponseGetSingleUser()

    result_response_get_user = ResponseGetSingleUser(response=reqresin.get(url="/api/users/2", verify=False))

    assert result_response_get_user.support_url == expected_response_get_user.support_url
    assert result_response_get_user.json == expected_response_get_user.json

def test_get_user_with_object_model(env):
    expected_response_get_user = ResponseGetSingleUser(data=ResponseUser(
        id=2,
        email="janet.weaver@reqres.in",
        first_name="Janet",
        last_name="Weaver",
        avatar="https://reqres.in/img/faces/2-image.jpg"
    ))

    result_response_get_user = Reqres(env).get_user(2)

    assert result_response_get_user.support_url == expected_response_get_user.support_url