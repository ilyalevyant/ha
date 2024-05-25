import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import uuid


import requests
from pytest import fixture

from automation_tests.api.services.authorization_service.authorization_service_helper import AuthorizationServiceHelper
from automation_tests.api.services.scrapper_service.config import Config as ScrapperConfig
from automation_tests.api.services.authorization_service.config import Config as AuthorizationConfig
from automation_tests.ui.services.authorization_service.pages.login_page import LoginPage
from automation_tests.ui.services.test_helpers.config import Config as UIConfig
from automation_tests.api.services.scrapper_service.scrapper_service_helper import ScraperServiceHelper
from automation_tests.ui.services.test_helpers.driver_factory import DriverFactory


@fixture
def authorization_service(service_session, authorization_service_conf):
    return AuthorizationServiceHelper(service_session, authorization_service_conf)


@fixture
def scraper_service(service_session, authorization_service_conf):
    return ScraperServiceHelper(service_session, scraper_service_conf)


@fixture
def authorization_service_conf():
    return AuthorizationConfig('qa')


@fixture
def scraper_service_conf():
    return ScrapperConfig('qa')


@fixture
def service_session():
    session = requests.Session()
    session.get("http://localhost:8000/accounts/register")
    csrf_token = session.cookies.get('csrftoken')
    session.post("http://localhost:8000/accounts/register/", {
            "csrfmiddlewaretoken": csrf_token,
            "username": str(uuid.uuid1())[0:8],
            "password1": "DRqmdeaZF@1",
            "password2": "DRqmdeaZF@1",
            "submit": "Submit"
    }, headers={'X-CSRFToken': csrf_token})
    return session


@fixture
def browser(ui_conf):
    driver_factory = DriverFactory(ui_conf)
    driver = driver_factory.get_driver()
    yield driver
    driver.quit()


@fixture
def login_page(browser, ui_conf):
    browser.get(ui_conf.login_page)
    return LoginPage(browser)


@fixture
def ui_conf():
    return UIConfig
