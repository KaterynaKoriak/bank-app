import allure
import pytest
from steps.api_steps.user_api_steps import user_api_steps, user_api_assert_steps


@allure.description('RGA-1')
@allure.title("Register customer via API")
@allure.tag('Account API')
def test_register_user(user_scenario, clear_initialize_db):
    user_api_steps.register_user(user_scenario.user_data)
    user_api_steps.get_user_info(user_scenario.customer_id)
    user_api_assert_steps.check_user_data(user_scenario.customer_id, user_scenario.user_data.customer)


@allure.description('RGA-2')
@allure.title("Edit User's data via API")
@allure.tag('Account API')
def test_update_user_info(user_scenario):
    user_api_steps.update_customer_info(user_scenario.customer_id, user_scenario.user_data.customer)
    user_api_assert_steps.check_user_data(user_scenario.customer_id, user_scenario.user_data.customer)


@allure.description('RGA-3')
@allure.title("New user has an account after creation")
@allure.tag('Account API')
def test_get_customer_accounts_info(user_scenario,  clear_initialize_db):
    user_api_steps.register_user(user_scenario.user_data)
    customer_id = user_api_steps.get_customer_accounts_info(user_scenario.customer_id).json()[0]['customerId']
    user_api_assert_steps.check_new_users_account(customer_id)
