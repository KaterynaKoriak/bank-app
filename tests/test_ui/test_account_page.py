import allure
import pytest
from steps.ui_steps.account_page_steps import account_page_steps, account_page_assert_steps
from constants.variables import TEST_INITIAL_BALANCE, DEFAULT_MIN_BALANCE, DEFAULT_BALANCE
from constants.variables import test_messages


@allure.description('ACU-1')
@allure.title('Associated with the user account is created')
@allure.tag('Account Page')
@pytest.mark.usefixtures('driver')
def test_account_creation(edit_default_admin_values, register_user, login, user_scenario):
    account_page_steps.navigate_to_accounts_overview()
    account_page_assert_steps.check_balance(TEST_INITIAL_BALANCE)
    account_page_assert_steps.check_total_balance(TEST_INITIAL_BALANCE)
    account_page_assert_steps.check_available_amount(TEST_INITIAL_BALANCE)


@allure.description('ACU-2')
@allure.title('Additional account can be created for User')
@allure.tag('Account Page')
@pytest.mark.usefixtures('driver')
def test_additional_account_creation(register_user, login, user_scenario):
    account_page_steps.navigate_to_open_new_account()
    account_page_assert_steps.check_accounts_overview_navigation(test_messages["open_account_title"])
    account_page_assert_steps.check_minimal_amount_message(DEFAULT_MIN_BALANCE)
    account_page_steps.create_savings_account()
    account_page_assert_steps.check_opened_account_title(test_messages["account_opened"])
    account_page_steps.navigate_to_accounts_overview()
    account_page_assert_steps.check_first_account_balance(DEFAULT_BALANCE, DEFAULT_MIN_BALANCE)
    account_page_assert_steps.check_second_account_balance(DEFAULT_MIN_BALANCE)

