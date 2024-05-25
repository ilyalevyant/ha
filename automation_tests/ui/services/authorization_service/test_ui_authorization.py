import uuid


def test_login(login_page):
    """
    1. Fill login form.
    2. Click on Login button.
    3. Validate according POST request with test data was sent from client to server.
    """
    random_username = str(uuid.uuid4())[0:8]
    random_password = str(uuid.uuid4())[0:12]
    login_page.login(random_username, random_password)
    login_page.validate_authorization_request(random_username, random_password)
