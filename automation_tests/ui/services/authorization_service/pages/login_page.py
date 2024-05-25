
from page_objects import PageObject, PageElement


class LoginPage(PageObject):

    __username_input: PageElement = PageElement(xpath="//*[./*[contains(text(), 'Username')]]//input")
    __password_input: PageElement = PageElement(xpath="//*[./*[contains(text(), 'Password')]]//input")
    __login_button: PageElement = PageElement(xpath="//*[@value='login']")

    def login(self, username: str = 'default_name', password: str = 'default_pass'):
        self.__username_input.send_keys(username)
        self.__password_input.send_keys(password)
        self.__login_button.click()

    def validate_authorization_request(self, username: str = 'default_name', password: str = 'default_pass'):
        authorization_request = None
        for request in self.w.requests:
            if request.method == 'POST' and request.path == '/accounts/login/':
                authorization_request = request
        assert authorization_request.params['username'] == username, f"Expected username: {username}, actual username: {authorization_request.params['username']}"
        assert authorization_request.params['password'] == password, f"Expected password: {password}, actual password: {authorization_request.params['password']}"

