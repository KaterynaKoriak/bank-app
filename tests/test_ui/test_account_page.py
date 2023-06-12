import allure
import pytest

from core.apps.frontend.pages.account_page import account_page
from steps.api_steps.account_api_steps import account_api_steps, account_api_assert_steps
from steps.ui_steps.account_page_steps import account_page_steps, account_page_assert_steps
from constants.variables import TEST_INITIAL_BALANCE, DEFAULT_MIN_BALANCE, DEFAULT_BALANCE, CUSTOMER_ID_STEP_DB, \
    FIRST_REGISTERED_CUSTOMER_ID
from constants.variables import test_messages, account_types
from steps.api_steps.user_api_steps import user_api_steps


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
    from_account_id = user_api_steps.get_customer_accounts_info(FIRST_REGISTERED_CUSTOMER_ID).json()[0]["id"]
    new_account_id = user_api_steps.create_account_for_existing_user(FIRST_REGISTERED_CUSTOMER_ID,
                                                                     account_types["CHECKING"],
                                                                     from_account_id).json()["id"]

    first_account_initial_balance = account_api_steps.get_account_balance(from_account_id)
    new_account_initial_balance = account_api_steps.get_account_balance(new_account_id)

    account_page_steps.navigate_to_transfer_funds()
    account_page_assert_steps.check_page_navigation(test_messages['transfer_funds_title'])

    list_of_id = account_page_steps.get_list_of_customer_accounts(FIRST_REGISTERED_CUSTOMER_ID)

    account_page_assert_steps.check_customers_accounts(list_of_id)
    account_page_steps.transfer_money(transfer_amount, from_account_id, new_account_id)
    account_page_assert_steps.check_transfer_complete_title(test_messages['transfer_complete_title'])
    account_page_steps.navigate_to_accounts_overview()

    first_account_balance_after_transaction = first_account_initial_balance - transfer_amount
    new_account_balance_after_transaction = new_account_initial_balance + transfer_amount

    account_page_assert_steps.check_account_balance_after_transaction(first_account_balance_after_transaction,
                                                                      allure_account_number="first")
    account_page_assert_steps.check_account_balance_after_transaction(new_account_balance_after_transaction,
                                                                      allure_account_number="new")


@allure.description('ACU-4')
@allure.title('User can pay a bill')
@allure.tag('Account Page')
@pytest.mark.usefixtures('driver')
@pytest.mark.parametrize('payment_amount', [10, 0, -10, 100.5])
@pytest.mark.parametrize('user_scenario', [2], indirect=True)
def test_bill_pay_ui(register_user, login, user_scenario, payment_amount):
    first_customer_account_id = user_api_steps.get_customer_accounts_info(FIRST_REGISTERED_CUSTOMER_ID).json()[0]["id"]
    first_customer_initial_balance = account_api_steps.get_account_balance(first_customer_account_id)

    second_customer_account_id = \
        user_api_steps.get_customer_accounts_info(FIRST_REGISTERED_CUSTOMER_ID + CUSTOMER_ID_STEP_DB).json()[0]["id"]
    second_registered_user_data = user_scenario[1]

    account_page_steps.navigate_to_bill_pay_screen()
    account_page_steps.send_bill_payment(second_registered_user_data, second_customer_account_id,
                                         first_customer_account_id,
                                         payment_amount)
    account_page_assert_steps.check_bill_payment_complete_title(test_messages['bill_payment_complete'])

    balance_after_transaction = first_customer_initial_balance - payment_amount
    account_page_steps.navigate_to_accounts_overview()
    account_page_assert_steps.check_account_balance_after_transaction(balance_after_transaction,
                                                                      allure_account_number='first')
    account_api_assert_steps.check_account_balance_after_transaction(first_customer_account_id,
                                                                     balance_after_transaction,
                                                                     allure_account_number='first')


@allure.description('ACU-5')
@allure.title('Request a loan')
@allure.tag('Account Page')
@pytest.mark.usefixtures('driver')
def test_loan_request(register_user, login, user_scenario):
    from_account_id = user_api_steps.get_customer_accounts_info(FIRST_REGISTERED_CUSTOMER_ID).json()[0]["id"]
    account_page_steps.navigate_to_request_loan()
    account_page_steps.fill_request_loan_form(100, 20, from_account_id)
    account_page_assert_steps.check_loan_request_confirmation_message()
    account_page_assert_steps.check_loan_provider()
    account_page_assert_steps.check_loan_status()
    account_page_assert_steps.check_loan_date()
    new_account = account_page.new_account_number().text
    account_page_steps.navigate_to_accounts_overview()
    account_page_assert_steps.check_account_is_created(new_account)
