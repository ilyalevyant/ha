import uuid
from dataclasses import dataclass

from automation_tests.api.services.authorization_service.authorization_service_api import AuthorizationServiceApi


@dataclass
class AuthorizationServiceHelper(AuthorizationServiceApi):

    def __post_init__(self):
        self.base_endpoint = self._authorization_service_conf.service_base_endpoint
        self.accounts_endpoint = f'{self.base_endpoint}/accounts'
        self.login_endpoint = f'{self.accounts_endpoint}/login/'
        self.logout_endpoint = f'{self.accounts_endpoint}/logout'
        self.register_endpoint = f'{self.accounts_endpoint}/register/'

        self.user_password = self._authorization_service_conf.USER_PASSWORD

    def create_user(self):
        user_name = str(uuid.uuid4())[0:12]
        r = self._post_authorization_service(self.register_endpoint, payload=self.payload_new_user(user_name))
        assert r.status_code == 200, "Failed to create new user"
        return user_name

    def login(self, user_name):
        r = self._post_authorization_service(self.login_endpoint, payload=self.payload_login(user_name))
        assert r.status_code == 200, f"Failed to login with user {user_name}"
        return r.text

    def payload_new_user(self, user_name):
        return {
            "username": user_name,
            "password1": self.user_password,
            "password2": self.user_password,
            "submit": "Submit"
        }

    def payload_login(self, user_name):
        return {
            "username": user_name,
            "password": self.user_password,
            "next": ""
        }
