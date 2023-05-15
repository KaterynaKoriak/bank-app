import allure
import pytest

from steps.api_steps.user_api_steps import user_api_steps, user_api_assert_steps
from constants.variables import INITIALIZED_DB_SECOND_CUSTOMER_ID, FIRST_REGISTERED_CUSTOMER_ID


@allure.description('RGA-1')
@allure.title("Register customer via API")
@allure.tag('Account API')
@pytest.mark.parametrize('user_scenario', [1], indirect=True)
def test_register_user(user_scenario):
    user_scenario = user_scenario[0]
    user_api_steps.register_user(user_scenario)
    user_api_steps.get_user_info(FIRST_REGISTERED_CUSTOMER_ID)
    user_api_assert_steps.check_user_data(FIRST_REGISTERED_CUSTOMER_ID,
                                          user_scenario.customer)


@allure.description('RGA-2')
@allure.title("Edit User's data via API")
@allure.tag('Account API')
@pytest.mark.parametrize('user_scenario', [1], indirect=True)
def test_update_user_info(user_scenario):
    user_scenario = user_scenario[0]
    user_api_steps.update_customer_info(INITIALIZED_DB_SECOND_CUSTOMER_ID,
                                        user_scenario.customer)
    user_api_assert_steps.check_user_data(INITIALIZED_DB_SECOND_CUSTOMER_ID,
                                          user_scenario.customer)


@allure.description('RGA-3')
@allure.title("New user has an account after creation")
@allure.tag('Account API')
@pytest.mark.parametrize('user_scenario', [1], indirect=True)
def test_get_customer_accounts_info(user_scenario):
    user_scenario = user_scenario[0]
    user_api_steps.register_user(user_scenario)
    user_api_assert_steps.check_new_users_account(FIRST_REGISTERED_CUSTOMER_ID)
