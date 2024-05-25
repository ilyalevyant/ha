
def test_create_user(authorization_service):
    user_name = authorization_service.create_user()
    r = authorization_service.login(user_name)
    assert "Please enter a correct username and password" not in r, f"user {user_name} was not logged in to the system"


def test_login_invalid_user(authorization_service):
    r = authorization_service.login("non-existing-user")
    assert "Please enter a correct username and password" in r, f"non-existing user logged in to the system"
