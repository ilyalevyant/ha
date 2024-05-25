from dataclasses import dataclass

from automation_tests.api.services.authorization_service.config import Config
from automation_tests.api.services.services_api.services_api import ServicesApi


@dataclass
class AuthorizationServiceApi(ServicesApi):
    _authorization_service_conf: Config

    def _get_authorization_service(self, endpoint):
        r = self._get(endpoint)
        return r

    def _post_authorization_service(self, endpoint, payload):
        r = self._post(endpoint, payload)
        return r
