import allure
import pytest
from addict import Dict
from core.testlib.utils import get_random_str
from steps.ui_steps.main_page_steps import main_page_steps, main_page_assert_steps


@allure.description('RGU-1')
@allure.title('Create user')
@allure.tag('Main Page')
@pytest.mark.parametrize("userdata, title", [({1: get_random_str(), 2: 'test', 3: '1234 Daisy Street', 4: 'Cincinnati',
                                               5: 'Ohio', 6: 12345, 7: 1234567890, 8: 987654321, 9: get_random_str(),
                                               10: 'password', 11: 'password'}, "ParaBank | Customer Created")])
@pytest.mark.usefixtures('driver')
def test_registration(userdata, title):
    main_page_steps.fill_form(userdata[1], userdata[2], userdata[3],userdata[4], userdata[5], userdata[6], userdata[7],
                              userdata[8], userdata[9], userdata[10], userdata[11])
    main_page_assert_steps.check_welcome_username(userdata[9])
    main_page_assert_steps.check_welcome_full_name(userdata[1], userdata[2])
    main_page_assert_steps.check_welcome_page_navigation(title)


@allure.description('RGU-2')
@allure.title('Create user with duplicated username')
@allure.tag('Main Page')
@pytest.mark.parametrize("error_message, userdata", [("This username already exists.",
                         {1: get_random_str(), 2: 'test', 3: '1234 Daisy Street', 4: 'Cincinnati', 5: 'Ohio', 6: 12345,
                          7: 1234567890, 8: 987654321, 9: 'k0_tt', 10: 'password', 11: 'password'})])
@pytest.mark.usefixtures('driver')
def test_user_with_duplicated_username(userdata, error_message):
    main_page_steps.fill_form(userdata[1], userdata[2], userdata[3], userdata[4], userdata[5], userdata[6],
                              userdata[7], userdata[8], userdata[9], userdata[10], userdata[11])
    main_page_assert_steps.check_existing_username_error_message(error_message)


@allure.description('RGU-3')
@allure.title('Create user with empty password field')
@allure.tag('Main Page')
@pytest.mark.parametrize("password_error_message, confirm_password_error_message, userdata",
                         [("Password is required.", "Password confirmation is required.",
                            {1: get_random_str(), 2: 'test', 3: '1234 Daisy Street', 4: 'Cincinnati', 5: 'Ohio',
                             6: 12345, 7: 1234567890, 8: 987654321, 9: get_random_str(), 10: '', 11: ''})])
@pytest.mark.usefixtures('driver')
def test_user_with_empty_password(userdata, password_error_message, confirm_password_error_message):
    main_page_steps.fill_form(userdata[1], userdata[2], userdata[3], userdata[4], userdata[5], userdata[6],
                              userdata[7], userdata[8], userdata[9], userdata[10], userdata[11])
    main_page_assert_steps.check_empty_password_error_message(password_error_message)
    main_page_assert_steps.check_confirm_password_error_message(confirm_password_error_message)


@allure.description('RGU-4')
@allure.title('Create user with different confirm password')
@allure.tag('Main Page')
@pytest.mark.parametrize("not_matched_confirm_password_error_message, userdata",
                         [("Passwords did not match.",
                          {1: get_random_str(), 2: 'test', 3: '1234 Daisy Street', 4: 'Cincinnati', 5: 'Ohio', 6: 12345,
                           7: 1234567890, 8: 987654321, 9: get_random_str(), 10: 'password', 11: 'pssword'})])
@pytest.mark.usefixtures('driver')
def test_user_with_different_confirm_password(userdata, not_matched_confirm_password_error_message):
    main_page_steps.fill_form(userdata[1], userdata[2], userdata[3], userdata[4], userdata[5], userdata[6],
                              userdata[7], userdata[8], userdata[9], userdata[10], userdata[11])
    main_page_assert_steps.check_confirm_password_error_message(not_matched_confirm_password_error_message)
    