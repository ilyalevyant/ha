
from dataclasses import dataclass

from automation_tests.api.services.scrapper_service.scrapper_service_api import ScraperServiceApi


@dataclass
class ScraperServiceHelper(ScraperServiceApi):

    def __post_init__(self):
        self.base_endpoint = 'http://localhost:8000'
        self.feeds_endpoint = f'{self.base_endpoint}/feeds'
        self.accounts_endpoint = f'{self.base_endpoint}/accounts'
        self.new_feed_endpoint = f'{self.feeds_endpoint}/new/'
        self.my_feed_endpoint = f'{self.feeds_endpoint}/my'

    def create_feed(self):
        r = self._post_scraper_service(self.new_feed_endpoint, payload=self.payload_feed())
        assert r.status_code == 200, "Failed to create new feed"
        return r

    def get_all_feeds(self):
        r = self._get_scraper_service(self.feeds_endpoint)
        assert r.status_code == 200, "Failed to get all feeds"
        return r.text

    def add_comment(self, entry_id, comment):
        r = self._post_scraper_service(f'{self.feeds_endpoint}/{entry_id}/entry/', payload=self.payload_comment(comment, entry_id))
        assert r.status_code == 200, f"commment was not added to the entry {entry_id}"

    def get_comments(self, entry_id):
        r = self._get_scraper_service(f'{self.feeds_endpoint}/{entry_id}/entry')
        assert r.status_code == 200, f"Failed to get comments by entry {entry_id}"
        return r.text

    def payload_comment(self, comment, entry_id):
        return {
                "content": comment,
                "submit": "Submit",
                "entry": entry_id
        }

    def payload_feed(self):
        return {
                # "feed_url": self.rss_feed_mock_url,
                "feed_url": "http://www.nu.nl/rss/Algemeen",
                "submit": "Submit"
        }
