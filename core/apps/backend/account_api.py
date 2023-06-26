import allure
from requests import Response

from core.apps.backend.user_api import WebApi


class AccountApi(WebApi):

    @allure.step("Pay bill")
    def post_bill_payment(self, userdata, amount: int, to_account_id: str, from_account_id: int) -> Response:
        data = {
            "name": f'{userdata.customer.firstName} {userdata.customer.lastName}',
            "address": {
                "street": userdata.customer.address.street,
                "city": userdata.customer.address.city,
                "state": userdata.customer.address.state,
                "zipCode": userdata.customer.address.zipCode
            },
            "phoneNumber": userdata.customer.phoneNumber,
            "accountNumber": to_account_id
        }

        params = {
            'accountId': from_account_id,
            'amount': amount
        }
        return self.api_post('/billpay', json=data, params=params)

    @allure.step("Get account info")
    def get_account_info(self, account_id: int) -> Response:
        params = {
            'accountId': account_id
        }
        return self.api_get(f'/accounts/{account_id}', params=params)

    @allure.step("Transfer money between user's accounts")
    def post_transfer(self, from_account_id: int, to_account_id: int, amount: int):
        params = {
            'fromAccountId': from_account_id,
            'toAccountId': to_account_id,
            'amount': amount
        }
        return self.api_post('/transfer', params=params)


account_api = AccountApi()
