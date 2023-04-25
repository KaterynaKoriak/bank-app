import allure
import pytest
from addict import Dict
from core.testlib.utils import get_random_str
from steps.api_steps.user_api_steps import user_api_steps, user_api_assert_steps


@allure.description('RGA-1')
@allure.title("Register customer via API")
@allure.tag('Account API')
@pytest.mark.parametrize('scenario', [
    Dict(customer_id=12434, repeatedPassword='password',
         customer=(Dict(firstName=get_random_str(), lastName='test', address=Dict(
             street='1 Rose Street', city='New York City', state='New York',
             zipCode='11111'), phoneNumber='987654321', ssn='123456789',
                        username=get_random_str(), password='password')))])
def test_register_user(scenario):
    user_api_steps.clean_db()
    user_api_steps.initialize_db()
    user_api_steps.register_user(scenario)
    user_api_steps.get_user_info(scenario.customer_id)
    user_api_assert_steps.check_user_data(12434, scenario.customer)


@allure.description('RGA-2')
@allure.title("Edit User's data via API")
@allure.tag('Account API')
@pytest.mark.parametrize('scenario',
                         [Dict(customer_id=12323, user_data=Dict(firstName='Cindy', lastName='test', address=Dict(
                             street='1234 Daisy Street',
                             city='Cincinnati', state='Ohio',
                             zipCode='12345'), phoneNumber='1234567890',
                                                                 ssn='987654321',
                                                                 username='Cindy_test',
                                                                 password='password'))])
def test_update_user_info(scenario):
    user_api_steps.clean_db()
    user_api_steps.initialize_db()
    user_api_steps.update_customer_info(scenario.customer_id, scenario.user_data)
    user_api_assert_steps.check_user_data(scenario.customer_id, scenario.user_data)


@allure.description('RGA-3')
@allure.title("New user has an account after creation")
@allure.tag('Account API')
@pytest.mark.parametrize('scenario', [
    Dict(customer_id=12434, repeatedPassword='password',
         customer=(Dict(firstName=get_random_str(), lastName='test', address=Dict(
             street='1 Rose Street', city='New York City', state='New York',
             zipCode='11111'), phoneNumber='987654321', ssn='123456789',
                        username=get_random_str(), password='password')))])
def test_get_customer_accounts_info(scenario):
    user_api_steps.clean_db()
    user_api_steps.initialize_db()
    user_api_steps.register_user(scenario)
    customer_id = user_api_steps.get_customer_accounts_info(scenario.customer_id).json()[0]['customerId']
    user_api_assert_steps.check_new_users_account(customer_id)
