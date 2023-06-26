import allure
import pytest

from steps.api_steps.account_api_steps import account_api_steps, account_api_assert_steps
from steps.api_steps.user_api_steps import user_api_steps
from constants.variables import FIRST_REGISTERED_CUSTOMER_ID, CUSTOMER_ID_STEP_DB, SUCCESS_CODE, account_types


@allure.description('ACA-1')
@allure.title('Send funds via API')
@allure.tag('Account Page')
@pytest.mark.parametrize('payment_amount', [10, 100.5, -10, 0])
def test_send_funds_api(register_user, user_scenario, payment_amount):
    first_account_id = user_api_steps.get_customer_accounts_info(FIRST_REGISTERED_CUSTOMER_ID).json()[0]["id"]
    second_account_id = user_api_steps.create_account_for_existing_user(FIRST_REGISTERED_CUSTOMER_ID,
                                                                        account_types["CHECKING"],
                                                                        first_account_id).json()["id"]

    initial_first_account_balance = account_api_steps.get_account_balance(first_account_id)
    initial_second_account_balance = account_api_steps.get_account_balance(second_account_id)

    account_api_steps.transfer_money_api(first_account_id, second_account_id, payment_amount)

    first_account_balance_after_transaction = initial_first_account_balance - payment_amount
    second_account_balance_after_transaction = initial_second_account_balance + payment_amount

    account_api_assert_steps.check_account_balance_after_transaction(first_account_id,
                                                                     first_account_balance_after_transaction,
                                                                     allure_account_number='first')
    account_api_assert_steps.check_account_balance_after_transaction(second_account_id,
                                                                     second_account_balance_after_transaction,
                                                                     allure_account_number='second')


@allure.description('ACA-2')
@allure.title('Make bill payment via API')
@allure.tag('Account Page')
@pytest.mark.parametrize('payment_amount', [10, 100.5, -10, 0])
@pytest.mark.parametrize('user_scenario', [2], indirect=True)
def test_bill_pay_api(register_user, user_scenario, payment_amount):
    first_customer_account_id = user_api_steps.get_customer_accounts_info(FIRST_REGISTERED_CUSTOMER_ID).json()[0]["id"]
    initial_first_account_balance = account_api_steps.get_account_balance(first_customer_account_id)

    second_customer_account_id = \
        user_api_steps.get_customer_accounts_info(FIRST_REGISTERED_CUSTOMER_ID + CUSTOMER_ID_STEP_DB).json()[0]["id"]
    initial_second_account_balance = account_api_steps.get_account_balance(second_customer_account_id)
    second_registered_user_data = user_scenario[1]

    bill_payment_status_code = account_api_steps.send_bill_pay(second_registered_user_data, payment_amount,
                                                               second_customer_account_id,
                                                               first_customer_account_id).status_code
    account_api_assert_steps.check_bill_payment_complete_with_api(bill_payment_status_code, SUCCESS_CODE)

    first_user_balance_after_transaction = initial_first_account_balance - payment_amount
    second_user_balance_after_transaction = initial_second_account_balance + payment_amount

    account_api_assert_steps.check_account_balance_after_transaction(first_customer_account_id,
                                                                     first_user_balance_after_transaction,
                                                                     allure_account_number='first')
    account_api_assert_steps.check_account_balance_after_transaction(second_customer_account_id,
                                                                     second_user_balance_after_transaction,
                                                                     allure_account_number='second')
