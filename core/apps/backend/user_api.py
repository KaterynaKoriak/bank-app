import allure
from requests import Response
from addict import Dict
from config.env import API_URL
from core.apps.backend.base_api import BaseApi


class UserAccountApi(BaseApi):
    api_url = API_URL

    @allure.step("Get customer's accounts info")
    def get_customer_accounts(self, customer_id: int) -> Response:
        params = {
            'customerId': customer_id
        }
        return self.api_get(f'/customers/{customer_id}/accounts', params=params)

    @allure.step("Post customer's updated data")
    def update_user_info(self, customer_id: int, user_data: Dict) -> Response:
        params = {
            'firstName': user_data.firstName,
            'lastName': user_data.lastName,
            'street': user_data.address.street,
            'city': user_data.address.city,
            'state': user_data.address.state,
            'zipCode': user_data.address.zipCode,
            'phoneNumber': user_data.phoneNumber,
            'ssn': user_data.ssn,
            'username': user_data.username,
            'password': user_data.password
        }
        return self.api_post(f'/customers/update/{customer_id}', params=params)

    @allure.step("Get customer's data")
    def get_customer_info(self, customer_id: int) -> Response:
        params = {
            'customerId': customer_id
        }
        return self.api_get(f'/customers/{customer_id}', params=params)

    @allure.step("Create account for existing customer")
    def post_account(self, customer_id: int, new_account_type: str, from_account_id: int) -> Response:
        data = {
            'customerId': customer_id,
            'newAccountType': new_account_type,
            'fromAccountId': from_account_id
        }
        return self.api_post('/createAccount', json=data)

    @allure.step("Log in")
    def log_in(self, username: str, password: str) -> Response:
        return self.api_get(f'/login/{username}/{password}')

    @allure.step("Clean Database")
    def clean_database(self):
        return self.api_post('/cleanDB')

    @allure.step("Initialize Database")
    def initialize_database(self):
        return self.api_post('/initializeDB')


user_account_api = UserAccountApi()

