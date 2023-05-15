import allure
from addict import Dict
from hamcrest import equal_to
from requests import Response
from constants.variables import DEFAULT_BALANCE
from core.apps.backend.ui_api import ui_api

from core.apps.backend.user_api import user_account_api
from core.testlib.matchers import check_that


class UserApiSteps:
    @allure.step("Get info about customer's accounts")
    def get_customer_accounts_info(self, customer_id: int) -> Response:
        return user_account_api.get_customer_accounts(customer_id)

    @allure.step("Create new account for existing customer upon API")
    def create_account_for_existing_user(self, customer_id: int, new_account_type: str, from_account_id: int) -> Response:
        return user_account_api.post_account(customer_id, new_account_type, from_account_id)

    @allure.step("Change customer's data upon API")
    def update_customer_info(self, customer_id: int, user_data: Dict) -> Response:
        return user_account_api.update_user_info(customer_id, user_data)

    @allure.step("Get customer's data upon API")
    def get_user_info(self, customer_id: int) -> Response:
        return user_account_api.get_customer_info(customer_id)

    @allure.step("Register customer upon API")
    def register_user(self, user_data: Dict) -> Response:
        ui_api.get_registration()
        return ui_api.post_registration(user_data)

    @allure.step('Clean DB')
    def clean_db(self):
        return user_account_api.clean_database()

    @allure.step('Initialize DB')
    def initialize_db(self):
        return user_account_api.initialize_database()


user_api_steps = UserApiSteps()


class UserApiAssertSteps:
    @allure.step("Check that changed upon API User's data corresponds to the current data")
    def check_user_data(self, customer_id: int, user_data: Dict) -> None:
        customer_api = user_api_steps.get_user_info(customer_id).json()
        check_that(customer_api.get('firstName'), equal_to(user_data.firstName),
                   f'Customer first name is {user_data.firstName}')
        check_that(customer_api.get('lastName'), equal_to(user_data.lastName),
                   f'Customer lastName is {user_data.lastName}')
        check_that(customer_api.get('address').get('street'), equal_to(user_data.address.street),
                   f'Customer street is {user_data.address.street}')
        check_that(customer_api.get('address').get('city'), equal_to(user_data.address.city),
                   f'Customer city is {user_data.address.city}')
        check_that(customer_api.get('address').get('state'), equal_to(user_data.address.state),
                   f'Customer state is {user_data.address.state}')
        check_that(customer_api.get('address').get('zipCode'), equal_to(user_data.address.zipCode),
                   f'Customer zipCode is {user_data.address.zipCode}')
        check_that(customer_api.get('phoneNumber').lstrip(" , +"), equal_to(user_data.phoneNumber.lstrip("+, ")),
                   f'Customer phone number is {user_data.phoneNumber}')
        check_that(customer_api.get('ssn'), equal_to(user_data.ssn), f'Customer ssn is {user_data.ssn}')

    @allure.step("Check that user has account after creation upon API")
    def check_new_users_account(self, customer_id: int) -> None:
        customer_api = user_api_steps.get_customer_accounts_info(customer_id).json()
        check_that(lambda: customer_api[0].get('balance'), equal_to(DEFAULT_BALANCE),
                   f'Customer has {DEFAULT_BALANCE} on his account')
        check_that(len(customer_api), equal_to(1), 'Customer has only one account')


user_api_assert_steps = UserApiAssertSteps()
