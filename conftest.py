import allure
import pytest
from selene.support.shared import browser
from selenium.webdriver.remote.webdriver import WebDriver

from core.apps.frontend.pages.main_page import main_page
from core.testlib import driver as driver_setup
from core.testlib.logger import LOGGER


@pytest.fixture(scope='function')
def driver() -> WebDriver:
    LOGGER.info(f'Starting driver')
    ui_driver = driver_setup.Driver().start()
    browser.config.driver = ui_driver
    LOGGER.info(f'Driver started')
    main_page.navigate()

    yield ui_driver

    ui_driver.quit()
    LOGGER.info(f'Driver quit')


def pytest_exception_interact(node, call, report):
    """Attach screenshot if test failed"""
    if report.failed:
        try:
            with open(browser.config.last_screenshot, 'rb') as screen:
                allure.attach(screen.read(), 'screen', allure.attachment_type.PNG)
        except TypeError:
            LOGGER.info('No screenshots for the issue')
