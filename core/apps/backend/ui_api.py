import allure
import urllib3
from addict import Dict
from requests import Response

from config.env import BASE_URL
from core.apps.backend.base_api import BaseApi
from core.testlib.utils import get_random_int


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class UIApi(BaseApi):
    api_url = BASE_URL

    def get_registration(self):
        return self.api_get("/register.htm")

    @allure.step("Register new customer")
    def post_registration(self, user_data: Dict) -> Response:
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
            'repeatedPassword': user_data.repeatedPassword
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        return self.api_post(f'/register.htm', data=data, headers=headers)

    def get_admin_page(self):
        return self.api_get("/admin.htm")

    @allure.step("Change default values from admin page")
    def post_admin_changes(self, initial_balance, min_balance):
        data = {
            'accessMode': 'jdbc',
            'initialBalance': initial_balance,
            'minimumBalance': min_balance,
            'loanProvider': 'ws',
            'loanProcessor': 'funds',
            'loanProcessorThreshold': 20
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        return self.api_post("/admin.htm", data=data, headers=headers)



ui_api = UIApi()
