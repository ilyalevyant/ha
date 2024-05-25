from dataclasses import dataclass

from automation_tests.api.services.scrapper_service.config import Config
from automation_tests.api.services.services_api.services_api import ServicesApi


@dataclass
class ScraperServiceApi(ServicesApi):
    _scraper_service_conf: Config

    def _get_scraper_service(self, endpoint):
        r = self._get(endpoint)
        return r

    def _post_scraper_service(self, endpoint, payload):
        r = self._post(endpoint, payload)
        return r
