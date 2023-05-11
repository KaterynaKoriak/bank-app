import allure
from hamcrest import equal_to

from core.testlib.matchers import check_that
from core.apps.frontend.pages.account_page import account_page
from core.testlib.helpers.api_helpers import format_two_digits_after_comma
from constants.variables import test_messages
from core.apps.backend.user_api import user_account_api


class AccountPageSteps:
    @allure.step('Navigate to the Open New Account page')
    def navigate_to_open_new_account(self) -> None:
        account_page.click_open_new_account_link()

    @allure.step('Create New Account')
    def create_savings_account(self) -> None:
        account_page.open_account_type_dropdown()
        account_page.select_savings_account_type()
        account_page.click_open_new_account_button()

    @allure.step('Navigate to the Accounts Overview')
    def navigate_to_accounts_overview(self) -> None:
        account_page.click_accounts_overview_option()

    @allure.step('Navigate to the Transfer Funds')
    def navigate_to_transfer_funds(self) -> None:
        account_page.click_transfer_funds()

    @allure.step("Get list of customer's account with API")
    def get_list_of_customer_accounts(self, customer_id):
        accounts = user_account_api.get_customer_accounts(customer_id).json()
        return [account["id"] for account in accounts]

    @allure.step('Transfer money')
    def transfer_money(self, transfer, from_account_id, to_account_id) -> None:
        account_page.fill_transfer_amount_input(transfer)
        account_page.click_from_account_dropdown()
        account_page.select_from_account(from_account_id, account_page.from_account_dropdown_items)
        account_page.click_to_account_dropdown()
        account_page.select_to_account(to_account_id, account_page.to_account_dropdown_items)
        account_page.click_transfer_button()


account_page_steps = AccountPageSteps()


class AccountPageAssertSteps:
    @allure.step('Check total balance on the Account overview page')
    def check_total_balance(self, initial_balance):
        check_that(account_page.accounts_overview_total().text,
                   equal_to(f"${format_two_digits_after_comma(initial_balance)}"),
                   f'Account total balance =${initial_balance}')

    @allure.step('Check balance on the Account overview page')
    def check_balance(self, initial_balance):
        balance = account_page.get_accounts_overview_balance(format_two_digits_after_comma(initial_balance))
        check_that(lambda: balance().text, (f"${format_two_digits_after_comma(initial_balance)}"),
                   f'Account balance = ${initial_balance}')

    @allure.step('Check available amount on the Account overview page')
    def check_available_amount(self, initial_balance):
        available_amount = account_page.get_accounts_overview_available_amount(
            format_two_digits_after_comma(initial_balance))
        check_that(available_amount().text, equal_to(f"${format_two_digits_after_comma(initial_balance)}"),
                   f'Available amount = ${initial_balance}')

    @allure.step('Check page title')
    def check_page_navigation(self, title):
        check_that(lambda: account_page.page_meta_title().get_attribute("innerHTML"), equal_to(title),
                   f'page title is "{title}"')

    @allure.step('Check the minimal amount in the message on the Open new account page')
    def check_minimal_amount_message(self, min_balance):
        check_that(account_page.minimal_amount_message().text,
                   equal_to(test_messages['minimal_amount_message'].format(min_balance)),
                   f'"${format_two_digits_after_comma(min_balance)}" is in the message on the Open new account page')

    @allure.step('Check the title "Account Opened!" is displayed')
    def check_opened_account_title(self, title):
        check_that(lambda: account_page.page_title().text, equal_to(title), "the title is 'Account Opened!'")

    @allure.step('Check that the first account has "initial balance - minimal balance" amount of money')
    def check_first_account_balance(self, initial_balance, minimal_balance):
        actual_balance = initial_balance - minimal_balance
        balance_value = account_page.get_accounts_overview_balance(format_two_digits_after_comma(actual_balance))
        check_that(lambda: balance_value().text, equal_to(f'${format_two_digits_after_comma(actual_balance)}'),
                   f'${actual_balance} is the balance on the first account')

    @allure.step('Check that the second account has "minimal balance" amount of money')
    def check_second_account_balance(self, minimal_balance):
        balance_value = account_page.get_accounts_overview_balance(format_two_digits_after_comma(minimal_balance))
        check_that(balance_value().text, equal_to(f'${format_two_digits_after_comma(minimal_balance)}'),
                   f'${minimal_balance} is the balance on the second account')

    @allure.step('Check that account numbers in the dropdown belong to the User')
    def check_customers_accounts(self, account_id_list):
        check_that(len(account_page.from_account_dropdown_items), equal_to(len(account_id_list)),
                   f'there are {len(account_page.from_account_dropdown_items)} accounts in dropdown that belong to the User')

    @allure.step('Check the title "Transfer Complete!" is displayed')
    def check_transfer_complete_title(self, title):
        check_that(lambda: account_page.page_title().text, equal_to(title), "the title is 'Transfer Complete!'")

    @allure.step('Check the balance after transaction')
    def check_account_balance_after_transaction(self, after_transaction_balance, **kwargs):
        balance_value = account_page.get_accounts_overview_balance(
            format_two_digits_after_comma(after_transaction_balance))
        for key in kwargs.keys():
            check_that(lambda: balance_value().text,
                       equal_to(f'${format_two_digits_after_comma(after_transaction_balance)}'),
                       f'${after_transaction_balance} is the balance on the {kwargs[key]} account')


account_page_assert_steps = AccountPageAssertSteps()
