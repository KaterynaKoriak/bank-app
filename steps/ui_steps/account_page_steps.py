import allure
from hamcrest import equal_to
from core.testlib.matchers import check_that
from core.apps.frontend.pages.account_page import account_page
from core.testlib.helpers.api_helpers import format_two_digits_after_comma


class AccountPageSteps:
    @allure.step('Log in')
    def login(self, user_data, password):
        account_page.fill_login_username_input(user_data.customer.username)
        account_page.fill_login_password_input(password)
        account_page.click_login_button()

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


account_page_steps = AccountPageSteps()


class AccountPageAssertSteps:
    @allure.step('Check total balance on the Account overview page')
    def check_total_balance(self, initial_balance):
        check_that(account_page.accounts_overview_total().text,
                   equal_to(f"${format_two_digits_after_comma(initial_balance)}"),
                   f'Account total balance =${initial_balance}')

    @allure.step('Check balance on the Account overview page')
    def check_balance(self, initial_balance):
        check_that(lambda: account_page.first_account_overview_balance().text,
                   equal_to(f"${format_two_digits_after_comma(initial_balance)}"),
                   f'Account balance = ${initial_balance}')

    @allure.step('Check available amount on the Account overview page')
    def check_available_amount(self, initial_balance):
        check_that(account_page.accounts_overview_available_amount().text,
                   equal_to(f"${format_two_digits_after_comma(initial_balance)}"),
                   f'Available amount = ${initial_balance}')

    @allure.step('Check page title')
    def check_accounts_overview_navigation(self, title):
        check_that(lambda: account_page.accounts_overview_title().get_attribute("innerHTML"), equal_to(title),
                   f'page title is "{title}"')

    @allure.step('Check the minimal amount in the message on the Open new account page')
    def check_minimal_amount_message(self, min_balance):
        check_that(account_page.minimal_amount_message().text, equal_to(
            f'A minimum of ${"{:.2f}".format(min_balance)} must be deposited into this account at time of opening.'
            f' Please choose an existing account to transfer funds into the new account.'),
                   f'minimal amount {format_two_digits_after_comma(min_balance)} is in the message on the Open new account page')

    @allure.step('Check the title "Account Opened!" is displayed')
    def check_opened_account_title(self, title):
        check_that(lambda: account_page.account_opened_title().text, equal_to(title), f'the title is "Account Opened!"')

    @allure.step('Check that the first account has "initial balance - minimal balance" amount of money')
    def check_first_account_balance(self, initial_balance, minimal_balance):
        actual_balance = initial_balance - minimal_balance
        check_that(lambda: account_page.first_account_overview_balance().text,
                   equal_to(f'${format_two_digits_after_comma(actual_balance)}'),
                   f'the first account has {actual_balance} on it balance')

    @allure.step('Check that the second account has "minimal balance" amount of money')
    def check_second_account_balance(self, minimal_balance):
        check_that(account_page.second_account_overview_balance().text,
                   equal_to(f'${format_two_digits_after_comma(minimal_balance)}'),
                   f'the second account has {minimal_balance} on it balance')


account_page_assert_steps = AccountPageAssertSteps()
