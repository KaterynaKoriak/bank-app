import datetime
import time

import allure
from hamcrest import equal_to
from selene import query

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

    @allure.step('Open Bill Pay screen')
    def navigate_to_bill_pay_screen(self):
        account_page.click_bill_pay_option()

    @allure.step('Enter payee information and send the form')
    def send_bill_payment(self, userdata, to_account_id, from_account_id, payment_amount):
        account_page.fill_payee_name_input(f'{userdata.customer.firstName} {userdata.customer.lastName}')
        account_page.fill_address_input(userdata.customer.address.street)
        account_page.fill_city_input(userdata.customer.address.city)
        account_page.fill_state_input(userdata.customer.address.state)
        account_page.fill_zip_code_input(userdata.customer.address.zipCode)
        account_page.fill_phone_input(userdata.customer.phoneNumber)
        account_page.fill_account_input(to_account_id)
        account_page.fill_verify_account_input(to_account_id)
        account_page.fill_amount_input(payment_amount)
        account_page.click_from_account_dropdown_bill()
        account_page.select_from_account(from_account_id, account_page.from_account_id_dropdown_options)
        account_page.click_send_payment()

    @allure.step('Navigate to the Open New Account page')
    def navigate_to_request_loan(self) -> None:
        account_page.click_request_loan_option()

    @allure.step('Apply for a loan')
    def fill_request_loan_form(self, loan_amount, down_amount, from_account_id):
        account_page.fill_loan_amount_input(loan_amount)
        account_page.fill_down_payment_input(down_amount)
        account_page.select_from_account(from_account_id, account_page.from_account_dropdown_items)
        account_page.click_apply_now()


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
        check_that(lambda: account_page.page_title().text, equal_to(title), f"the title is '{title}'")

    @allure.step('Check the balance after transaction')
    def check_account_balance_after_transaction(self, after_transaction_balance, allure_account_number):
        balance_value = account_page.get_accounts_overview_balance(
            format_two_digits_after_comma(after_transaction_balance))
        check_that(lambda: balance_value().text,
                   equal_to(f'${format_two_digits_after_comma(after_transaction_balance)}'),
                   f'${after_transaction_balance} is the balance on the {allure_account_number} account')

    @allure.step('Check the title "Bill Payment Complete!" is displayed')
    def check_bill_payment_complete_title(self, title):
        check_that(lambda: account_page.payment_complete_title.get(query.text), equal_to(title),
                   f"the title is '{title}'")

    @allure.step('Check the "Congratulations, your loan has been approved." message is displayed')
    def check_loan_request_confirmation_message(self):
        check_that(lambda: account_page.loan_request_confirmation_message().text,
                   equal_to(test_messages['loan_confirmation_message']),
                   f"confirmation message is '{test_messages['loan_confirmation_message']}'")

    @allure.step('Check the loan provider')
    def check_loan_provider(self):
        check_that(lambda: account_page.loan_provider().text, equal_to(test_messages['loan_provider']),
                   f"loan provider is '{test_messages['loan_provider']}'")

    @allure.step('Check the loan date')
    def check_loan_date(self):
        check_that(account_page.loan_date().text, equal_to(datetime.date.today().strftime("%m-%d-%Y")),
                   f"loan date is {account_page.loan_date().text}")

    @allure.step('Check the loan status')
    def check_loan_status(self):
        check_that(account_page.loan_status().text, equal_to('Approved'), "loan status is 'Approved'")

    @allure.step('The new account is created on the Accounts Overview page')
    def check_account_is_created(self, new_account):
        account = account_page.get_accounts_overview_account(new_account)
        check_that(lambda: account().text, equal_to(new_account), f"new account {new_account} is created")

    @allure.step('Verify account number')
    def check_account_number(self, account_id):
        check_that(lambda: int(account_page.account_id.get(query.text)), equal_to(account_id),
                   f"{account_id} is account id")

    @allure.step('Verify account type')
    def check_account_type(self, account_type):
        check_that(lambda: account_page.account_type.get(query.text), equal_to(account_type),
                   f"{account_type} is account type")

    @allure.step('Verify account balance')
    def check_account_balance(self, account_balance):
        check_that(lambda: account_page.account_balance.get(query.text),
                   equal_to(f"${format_two_digits_after_comma(account_balance)}"),
                   f"{account_balance} is account balance")

    @allure.step('Verify account available amount')
    def check_account_available_amount(self, account_available_amount):
        check_that(lambda: account_page.account_available_amount.get(query.text),
                   equal_to(f"${format_two_digits_after_comma(account_available_amount)}"),
                   f"{account_available_amount} is account available amount")

    @allure.step('Verify "All" account activity filters are selected')
    def check_account_activity_filters(self, selected_option):
        check_that(account_page.selected_transaction_type.get(query.text), equal_to(selected_option),
                   f"{selected_option} is selected transaction type")
        check_that(account_page.selected_accounts_activity_period.get(query.text), equal_to(selected_option),
                   f"{selected_option} is selected accounts activity period")

    @allure.step('Verify "Account Activity" table details')
    def check_transaction_info(self, number_of_transaction, transaction_amount, message):
        time.sleep(0.1)
        transaction_info = [element.get(query.text) for element in
                            account_page.get_transaction_info(number_of_transaction)]

        if message == test_messages["transfer_sent_message"]:
            debit_amount = f'${format_two_digits_after_comma(transaction_amount)}' if transaction_amount >= 0 \
                else f'-${format_two_digits_after_comma(abs(transaction_amount))}'
        else:
            debit_amount = ''
        if message == test_messages["transfer_received_message"]:
            credit_amount = f'${format_two_digits_after_comma(transaction_amount)}' if transaction_amount >= 0 \
                else f'-${format_two_digits_after_comma(abs(transaction_amount))}'
        else:
            credit_amount = ''
        expected_transaction_info = [datetime.date.today().strftime("%m-%d-%Y"), message, debit_amount, credit_amount]
        check_that(transaction_info, equal_to(expected_transaction_info), f"'Date' is {expected_transaction_info[0]}, "
                                                                          f"'Transaction' is '{message}', "
                                                                          f"'Debit(-)' is {debit_amount}, "
                                                                          f"'Credit(+)' is {credit_amount}")


account_page_assert_steps = AccountPageAssertSteps()
