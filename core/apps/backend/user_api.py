import allure
from requests import Response
from addict import Dict
from config.env import API_URL, URL
from core.apps.backend.base_api import BaseApi


class UserAccountApi(BaseApi):
    api_url = API_URL
    url = URL

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
            'street': user_data.street,
            'city': user_data.city,
            'state': user_data.state,
            'zipCode': user_data.zipCode,
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

    @allure.step("Register new customer")
    def register_new_customer(self, user_data: Dict) -> Response:
        data = {
            'customer.firstName': user_data.customer.firstName,
            'customer.lastName': user_data.customer.lastName,
            'customer.address.street': user_data.customer.address.street,
            'customer.address.city': user_data.customer.address.city,
            'customer.address.state': user_data.customer.address.state,
            'customer.address.zipCode': user_data.customer.address.zipCode,
            'customer.phoneNumber': user_data.customer.phoneNumber,
            'customer.ssn': user_data.customer.ssn,
            'customer.username': user_data.customer.username,
            'customer.password': user_data.customer.password,
            'repeatedPassword': user_data.password
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;"
                      "q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Cookie": "JSESSIONID=22CB8A2A043A0C6EF3BDDF7F427DF5BF"
        }
        return self.api_post_from_ui(f'/register.htm', data=data, headers=headers)

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

