import allure
import pytest
from steps.ui_steps.account_page_steps import account_page_steps, account_page_assert_steps
from constants.variables import TEST_INITIAL_BALANCE, DEFAULT_MIN_BALANCE, DEFAULT_BALANCE, \
    FIRSTLY_CREATED_USER_CUSTOMER_ID
from constants.variables import test_messages
from steps.api_steps.user_api_steps import user_api_steps
from core.testlib.helpers.api_helpers import get_text_from_json


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
    account_page_assert_steps.check_page_navigation(test_messages["open_account_title"])
    account_page_assert_steps.check_minimal_amount_message(DEFAULT_MIN_BALANCE)
    account_page_steps.create_savings_account()
    account_page_assert_steps.check_opened_account_title(test_messages["account_opened"])
    account_page_steps.navigate_to_accounts_overview()
    account_page_assert_steps.check_first_account_balance(DEFAULT_BALANCE, DEFAULT_MIN_BALANCE)
    account_page_assert_steps.check_second_account_balance(DEFAULT_MIN_BALANCE)


@allure.description('ACU-3')
@allure.title('User can transfer money between accounts')
@allure.tag('Account Page')
@pytest.mark.usefixtures('driver')
@pytest.mark.parametrize('transfer_amount', [10, 0, -10, 100.5])
def test_transfer_money_between_accounts(register_user, login, user_scenario, transfer_amount):
    from_account_id = \
     get_text_from_json(user_api_steps.get_customer_accounts_info(FIRSTLY_CREATED_USER_CUSTOMER_ID))[0]["id"]
    new_account_id = get_text_from_json(
        user_api_steps.post_account_for_existing_user(FIRSTLY_CREATED_USER_CUSTOMER_ID, 1, from_account_id))["id"]

    first_account_initial_balance = user_api_steps.get_account_balance(from_account_id)
    new_account_initial_balance = user_api_steps.get_account_balance(new_account_id)

    account_page_steps.navigate_to_transfer_funds()
    account_page_assert_steps.check_page_navigation(test_messages['transfer_funds_title'])
    account_page_steps.input_transfer_amount(transfer_amount)

    list_of_id = account_page_steps.get_list_of_customer_accounts(FIRSTLY_CREATED_USER_CUSTOMER_ID)

    account_page_assert_steps.check_customers_accounts(list_of_id)
    account_page_steps.select_from_account(from_account_id)
    account_page_steps.select_to_account(new_account_id)
    account_page_steps.transfer_money()
    account_page_assert_steps.check_transfer_complete_title(test_messages['transfer_complete_title'])
    account_page_steps.navigate_to_accounts_overview()

    first_account_balance_after_transaction = first_account_initial_balance - transfer_amount
    new_account_balance_after_transaction = new_account_initial_balance + transfer_amount

    account_page_assert_steps.check_account_balance_after_transaction(first_account_balance_after_transaction,
                                                                      "first")
    account_page_assert_steps.check_account_balance_after_transaction(new_account_balance_after_transaction, "new")
