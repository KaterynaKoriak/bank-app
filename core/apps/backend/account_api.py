import allure
from requests import Response

from config.env import API_URL
from core.apps.backend.base_api import BaseApi


class AccountApi(BaseApi):
    api_url = API_URL

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


account_api = AccountApi()
