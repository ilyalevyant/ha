from seleniumwire import webdriver
from dataclasses import dataclass
from automation_tests.ui.services.test_helpers.config import Config


@dataclass
class DriverFactory():
    config: Config = Config()

    def get_driver(self):
        conf = self.config
        driver = webdriver.Chrome()
        driver.set_window_size(conf.desktop_screen_width, conf.desktop_screen_height)
        driver.implicitly_wait(conf.implicitly_wait)
        return driver
