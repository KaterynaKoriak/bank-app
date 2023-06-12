import allure
from hamcrest import equal_to
from requests import Response

from core.apps.backend.account_api import account_api
from core.testlib.matchers import check_that


class AccountApiSteps:
    @allure.step("Send bill pay from 1 customer account to 2 customer account")
    def send_bill_pay(self, userdata, amount, to_account_id, from_account_id) -> Response:
        return account_api.post_bill_payment(userdata, amount, to_account_id, from_account_id)

    @allure.step("Get account balance")
    def get_account_balance(self, account_id: int):
        return account_api.get_account_info(account_id).json()["balance"]

    @allure.step("Transfer money")
    def transfer_money_api(self, from_account_id: int, to_account_id: int, amount: int):
        return account_api.post_transfer(from_account_id, to_account_id, amount)


account_api_steps = AccountApiSteps()


class AccountAssertSteps:
    @allure.step('Check that user payed the bill with API successfully')
    def check_bill_payment_complete_with_api(self, bill_payment_status_code, success_code):
        check_that(lambda: bill_payment_status_code, equal_to(success_code), f"the user pay bill successfully")

    @allure.step('Check that the account balance has changed')
    def check_account_balance_after_transaction(self, account_id, balance_after_transaction, allure_account_number):
        check_that(account_api_steps.get_account_balance(account_id), equal_to(balance_after_transaction),
                   f'${balance_after_transaction} is the balance on the {allure_account_number} account')


account_api_assert_steps = AccountAssertSteps()
