import uuid

from pytest import fixture


@fixture
def new_feed(scraper_service):
    """Creating feed instance"""
    return scraper_service.create_feed()


def test_update_feed(scraper_service, new_feed):
    """
    1. Get items from feed
    2. Add new item to feed source XML
    3. Send feed update request
    4. Get items from feed again
    5. Validate new item in response
    """
    pass


def test_get_all_feeds(scraper_service, new_feed):
    """
    1. Create new feed
    2. Get all feeds, validate this feed is in the list
    """
    r = scraper_service.get_all_feeds()
    assert "NU - Algemeen" in r, "new feed was not found in the response"


def test_comment_topic(scraper_service, new_feed):
    """
    1. Create feed
    2. Send post request to comment 1st topic
    3. Send get request to validate saved comment
    """
    comment = str(uuid.uuid4())[0:12]
    scraper_service.add_comment(entry_id="1", comment=comment)
    r = scraper_service.get_comments("1")
    assert comment in r, "added comment was not found in response"

