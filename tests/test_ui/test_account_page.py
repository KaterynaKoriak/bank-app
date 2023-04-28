# import allure
# import pytest
# from addict import Dict
# from core.testlib.utils import get_random_str
# from steps.ui_steps.account_page_steps import account_page_steps
#
#
# @allure.description('ACU-1')
# @allure.title('Associated with the user account is created')
# @allure.tag('Account Page')
# @pytest.mark.usefixtures('driver')
# def test_account_creation(changed_account_creation_default_values, register_user, login):
#     account_page_steps.navigate_to_open_new_account()
#     account_page_steps.create_new_account()
#     account_page_steps.navigate_to_accounts_overview()