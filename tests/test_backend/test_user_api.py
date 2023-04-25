import allure
import pytest
from addict import Dict

from steps.api_steps.user_api_steps import user_api_steps, user_api_assert_steps


@allure.description('RGA-1')
@allure.title("Register customer via API")
@allure.tag('Account API')
@pytest.mark.parametrize('scenario', [(Dict(customer=(Dict(firstName='Johnatan', lastName='test', address=Dict(
                                             street='1 Rose Street', city='New York City', state='New York',
                                             zipCode='11111'), phoneNumber='987654321', ssn='123456789',
                                             username='john_test', password='password', repeatedPassword='password'))))])
def test_register_user(scenario):
    #user_api_steps.clean_db()
    #user_api_steps.initialize_db()
    user_api_steps.register_user(scenario)
    user_api_steps.get_user_info(12767)
    user_api_assert_steps.check_user_data(12767, scenario)


@allure.description('RGA-2')
@allure.title("Edit User's data via API")
@allure.tag('Account API')
@pytest.mark.parametrize('customer_id, scenario', [(12323, Dict(firstName='Cindy', lastName='test',
                                                    street='1234 Daisy Street', city='Cincinnati', state='Ohio',
                                                    zipCode='12345', phoneNumber='1234567890', ssn='987654321',
                                                    username='Cindy_test', password='password'))])
def test_update_user_info(customer_id, scenario):
    user_api_steps.clean_db()
    user_api_steps.initialize_db()
    user_api_steps.update_customer_info(customer_id, scenario)
    user_api_assert_steps.check_user_data(customer_id, scenario)


@allure.description('RGA-3')
@allure.title("New user has an account after creation")
@allure.tag('Account API')
@pytest.mark.parametrize('customer_id', [12434])
def test_get_customer_accounts_info(customer_id):
    user_api_steps.get_customer_accounts_info(customer_id)
    user_api_assert_steps.check_new_users_account(customer_id)
