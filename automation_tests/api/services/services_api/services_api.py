from dataclasses import dataclass
import requests


@dataclass
class ServicesApi:
    __session: requests.Session()

    def _get(self, endpoint):
        return self.__session.get(endpoint)

    def _post(self, endpoint, payload):
        payload["csrfmiddlewaretoken"] = self._ServicesApi__session.cookies.get('csrftoken')
        return self.__session.post(endpoint, payload)
