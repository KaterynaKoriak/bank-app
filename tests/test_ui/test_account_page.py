import allure
import pytest
from steps.ui_steps.account_page_steps import account_page_steps, account_page_assert_steps
from core.testlib.helpers.account_decorators import register_user, edit_default_admin_values
from constants.variables import basic_password, test_initial_balance, test_min_balance, default_min_balance, \
    default_balance


@allure.description('ACU-1')
@allure.title('Associated with the user account is created')
@allure.tag('Account Page')
@pytest.mark.usefixtures('driver')
@edit_default_admin_values(initial_balance=test_initial_balance, min_balance=test_min_balance)
@register_user
def test_account_creation(user_scenario):
    account_page_steps.login(user_scenario, basic_password)
    account_page_steps.navigate_to_accounts_overview()
    account_page_assert_steps.check_balance(test_initial_balance)
    account_page_assert_steps.check_total_balance(test_initial_balance)
    account_page_assert_steps.check_available_amount(test_initial_balance)


@allure.description('ACU-2')
@allure.title('Additional account can be created for User')
@allure.tag('Account Page')
@pytest.mark.usefixtures('driver')
@register_user
def test_additional_account_creation(user_scenario):
    account_page_steps.login(user_scenario, basic_password)
    account_page_steps.navigate_to_open_new_account()
    account_page_assert_steps.check_accounts_overview_navigation("ParaBank | Open Account")
    account_page_assert_steps.check_minimal_amount_message(default_min_balance)
    account_page_steps.create_savings_account()
    account_page_assert_steps.check_opened_account_title("Account Opened!")
    account_page_steps.navigate_to_accounts_overview()
    account_page_assert_steps.check_first_account_balance(default_balance, default_min_balance)
    account_page_assert_steps.check_second_account_balance(default_min_balance)

