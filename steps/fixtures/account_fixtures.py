import pytest

from core.apps.backend.ui_api import ui_api
from constants.variables import DEFAULT_BALANCE, DEFAULT_MIN_BALANCE, TEST_INITIAL_BALANCE, TEST_MIN_BALANCE, \
    BASIC_PASSWORD
from core.apps.frontend.pages.account_page import account_page


@pytest.fixture(scope='function')
def register_user(user_scenario):
    ui_api.get_registration()
    for user in user_scenario:
        ui_api.post_registration(user)


@pytest.fixture(scope='function')
def edit_default_admin_values():
    ui_api.get_admin_page()
    ui_api.post_admin_changes(initial_balance=TEST_INITIAL_BALANCE, min_balance=TEST_MIN_BALANCE)
    yield
    ui_api.post_admin_changes(initial_balance=DEFAULT_BALANCE, min_balance=DEFAULT_MIN_BALANCE)


@pytest.fixture(scope='function')
def login(user_scenario):
    account_page.fill_login_username_input(user_scenario[0].customer.username)
    account_page.fill_login_password_input(BASIC_PASSWORD)
    account_page.click_login_button()
