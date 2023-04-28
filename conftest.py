import allure
import pytest
from selene.support.shared import browser
from selenium.webdriver.remote.webdriver import WebDriver
from core.apps.frontend.pages.main_page import main_page
from core.testlib import driver as driver_setup
from core.testlib.logger import LOGGER
from addict import Dict
from core.testlib.utils import get_random_last_name, get_random_first_name, get_random_city, get_random_state, \
    get_random_phone_number, get_random_ssn, get_random_str, get_random_zip_code, get_random_street
from core.apps.backend.user_api import user_account_api
from constants.variables import basic_password


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


@pytest.fixture(scope='function', autouse=True)
def clean_initialize_db():
    user_account_api.clean_database()
    user_account_api.initialize_database()


@pytest.fixture(scope='function')
def user_scenario():
    return Dict(repeatedPassword=basic_password,
                customer=(Dict(firstName=get_random_first_name(),
                               lastName=get_random_last_name(), address=Dict(
                        street=get_random_street(), city=get_random_city(),
                        state=get_random_state(),
                        zipCode=get_random_zip_code()),
                               phoneNumber=get_random_phone_number(),
                               ssn=get_random_ssn(),
                               username=get_random_str(),
                               password=basic_password)))


def pytest_exception_interact(node, call, report):
    """Attach screenshot if test failed"""
    if report.failed:
        try:
            with open(browser.config.last_screenshot, 'rb') as screen:
                allure.attach(screen.read(), 'screen', allure.attachment_type.PNG)
        except TypeError:
            LOGGER.info('No screenshots for the issue')
