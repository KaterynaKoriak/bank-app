import allure
import pytest
from addict import Dict
from core.testlib.utils import get_random_str
from steps.ui_steps.main_page_steps import main_page_steps, main_page_assert_steps


@allure.description('RGU-1')
@allure.title('Create user')
@allure.tag('Main Page')
@pytest.mark.parametrize('scenario', [Dict(first_name=get_random_str(), last_name='test', address='1234 Daisy Street',
                                           city='Cincinnati', state='Ohio', zip_code=12345, phone=1234567890,
                                           ssn=987654321, username=get_random_str(), password='password',
                                           confirmation_password='password')])
@pytest.mark.usefixtures('driver')
def test_registration(scenario):
    main_page_steps.fill_form(scenario)
    main_page_assert_steps.check_welcome_username(scenario.username)
    main_page_assert_steps.check_welcome_full_name(scenario.first_name, scenario.last_name)
    main_page_assert_steps.check_welcome_page_navigation("ParaBank | Customer Created")


@allure.description('RGU-2')
@allure.title('Create user with duplicated username')
@allure.tag('Main Page')
@pytest.mark.parametrize('scenario', [Dict(first_name=get_random_str(), last_name='test', address='1234 Daisy Street',
                                           city='Cincinnati', state='Ohio', zip_code=12345, phone=1234567890,
                                           ssn=987654321, username='kateryna_koriak', password='password',
                                           confirmation_password='password')])
@pytest.mark.usefixtures('driver')
def test_user_with_duplicated_username(scenario):
    main_page_steps.fill_form(scenario)
    main_page_assert_steps.check_existing_username_error_message("This username already exists.")


@allure.description('RGU-3')
@allure.title('Create user with empty password field')
@allure.tag('Main Page')
@pytest.mark.parametrize('scenario', [Dict(first_name=get_random_str(), last_name='test', address='1234 Daisy Street',
                                           city='Cincinnati', state='Ohio', zip_code=12345, phone=1234567890,
                                           ssn=987654321, username=get_random_str(), password='',
                                           confirmation_password='')])
@pytest.mark.usefixtures('driver')
def test_user_with_empty_password(scenario):
    main_page_steps.fill_form(scenario)
    main_page_assert_steps.check_empty_password_error_message("Password is required.")
    main_page_assert_steps.check_confirm_password_error_message("Password confirmation is required.")


@allure.description('RGU-4')
@allure.title('Create user with different confirm password')
@allure.tag('Main Page')
@pytest.mark.parametrize('scenario', [Dict(first_name=get_random_str(), last_name='test', address='1234 Daisy Street',
                                           city='Cincinnati', state='Ohio', zip_code=12345, phone=1234567890,
                                           ssn=987654321, username=get_random_str(), password='password',
                                           confirmation_password='passwod')])
@pytest.mark.usefixtures('driver')
def test_user_with_different_confirm_password(scenario):
    main_page_steps.fill_form(scenario)
    main_page_assert_steps.check_confirm_password_error_message("Passwords did not match.")
