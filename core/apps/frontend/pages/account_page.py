import allure
from selene import by, query
from selene.support.shared import browser

from core.apps.frontend.pages.base_page import BasePage


class AccountPage(BasePage):

    accounts_overview_link = browser.element(by.xpath("//a[contains(@href, '/parabank/overview.htm')]"))
    accounts_overview_total = browser.element(by.xpath("//b[@class='ng-binding']"))
    page_meta_title = browser.element(by.xpath("/html/head/title"))
    minimal_amount_message = browser.element(by.xpath("//select[@id='type']/following-sibling::p/b"))
    open_new_account = browser.element(by.xpath("//a[contains(@href, '/parabank/openaccount.htm')]"))
    page_title = browser.element(by.xpath("//h1[@class='title']"))
    account_type_dropdown = browser.element(by.xpath("//select[@id='type']"))
    savings_option = browser.element(by.xpath("//select[@id='type']/option[text()='SAVINGS']"))
    open_new_account_button = browser.element(by.xpath("//input[@value='Open New Account']"))
    first_name_input = browser.element(by.name("initialBalance"))
    submit_button = browser.element(by.xpath("//input[@value='Submit']"))
    login_username_input = browser.element(by.name("username"))
    login_password_input = browser.element(by.name("password"))
    login_button = browser.element(by.xpath("//input[@value='Log In']"))
    transfer_funds_option = browser.element(by.xpath("//li/a[text() = 'Transfer Funds']"))
    transfer_amount_input = browser.element(by.xpath("//input[@id='amount']"))
    from_account_dropdown = browser.element(by.xpath("//select[@id='fromAccountId']"))
    to_account_dropdown = browser.element(by.xpath("//select[@id='toAccountId']"))
    transfer_button = browser.element(by.xpath("//input[@value='Transfer']"))
    from_account_dropdown_items = browser.elements(by.xpath(f"//select[@id='fromAccountId']/option"))
    to_account_dropdown_items = browser.elements(by.xpath(f"//select[@id='toAccountId']/option"))

    bill_pay_option = browser.element(by.xpath("//a[text()='Bill Pay']"))
    payee_name_input = browser.element(by.xpath("//input[@ng-model='payee.name']"))
    address_input = browser.element(by.xpath("//input[@ng-model='payee.address.street']"))
    city_input = browser.element(by.xpath("//input[@ng-model='payee.address.city']"))
    state_input = browser.element(by.xpath("//input[@ng-model='payee.address.state']"))
    zip_code_input = browser.element(by.xpath("//input[@ng-model='payee.address.zipCode']"))
    phone_input = browser.element(by.xpath("//input[@ng-model='payee.phoneNumber']"))
    account_input = browser.element(by.xpath("//input[@ng-model='payee.accountNumber']"))
    verify_account_input = browser.element(by.xpath("//input[@ng-model='verifyAccount']"))
    amount_input = browser.element(by.xpath("//input[@ng-model='amount']"))
    from_account_id_dropdown = browser.element(by.xpath("//select[@name='fromAccountId']"))
    from_account_id_dropdown_options = browser.elements(by.xpath("//select[@name='fromAccountId']/option"))
    send_payment_button = browser.element(by.xpath("//input[@value='Send Payment']"))
    payment_complete_title = browser.element(by.xpath("//div[@ng-show='showResult']/h1[@class='title']"))
    request_loan_option = browser.element(by.xpath("//a[@href='/parabank/requestloan.htm']"))
    loan_amount_input = browser.element(by.xpath("//input[@id='amount']"))
    down_payment_input = browser.element(by.xpath("//input[@id='downPayment']"))
    apply_now_button = browser.element(by.xpath("//input[@value='Apply Now']"))
    loan_request_confirmation_message = browser.element(by.xpath("//p[contains(text(), 'Congratulations')]"))
    loan_provider = browser.element(by.id("loanProviderName"))
    loan_date = browser.element(by.id("responseDate"))
    loan_status = browser.element(by.id("loanStatus"))
    new_account_number = browser.element(by.id("newAccountId"))

    account_id = browser.element(by.id("accountId"))
    account_type = browser.element(by.id("accountType"))
    account_balance = browser.element(by.id("balance"))
    account_available_amount = browser.element(by.id("availableBalance"))
    selected_transaction_type = browser.element(by.xpath("//select[@id='transactionType']"
                                                         "/option[@selected='selected']"))
    selected_accounts_activity_period = browser.element(by.xpath("//select[@id='month']/option[@selected='selected']"))

    @staticmethod
    def get_transaction_info(number_of_transaction):
        return browser.elements(by.xpath(f"//tr[@ng-repeat='transaction in transactions']"
                                         f"[{number_of_transaction}]/td"))

    @staticmethod
    def get_accounts_overview_balance(text):
        return browser.element(by.xpath(f'//td[count(//th[.="Balance*"]/preceding-sibling::th)+1][text()="${text}"]'))

    @staticmethod
    def get_accounts_overview_available_amount(text):
        return browser.element(by.xpath(f'//td[count(//th[.="Available Amount"]'
                                        f'/preceding-sibling::th)+1][text()="${text}"]'))

    @staticmethod
    def get_accounts_overview_account(text):
        return browser.element(by.xpath(f'//td/a[count(//th[.="Account"]/preceding-sibling::th)+1][text()="{text}"]'))

    @staticmethod
    def get_dropdown_item(account_id, dropdown):
        return next(item for item in dropdown if item.get(query.text) == str(account_id))

    @allure.step('Click "Open New Account" option on the navigation panel')
    def click_open_new_account_link(self):
        self.open_new_account.click()

    @allure.step('Open account type dropdown')
    def open_account_type_dropdown(self):
        self.account_type_dropdown.click()

    @allure.step('Select "Savings" account type option')
    def select_savings_account_type(self):
        self.savings_option.click()

    @allure.step('Click "Open New Account" button')
    def click_open_new_account_button(self):
        self.open_new_account_button.click()

    @allure.step('Click "Accounts Overview" option on the navigation panel')
    def click_accounts_overview_option(self):
        self.accounts_overview_link.click()

    @allure.step('Fill in username input for customer login')
    def fill_login_username_input(self, text: str):
        self.login_username_input.send_keys(text)

    @allure.step('Fill in password input for customer login')
    def fill_login_password_input(self, text: str):
        self.login_password_input.send_keys(text)

    @allure.step('Click on "Log in" button')
    def click_login_button(self):
        self.login_button.click()

    @allure.step('Click the "Transfer Funds" option on the left navigation panel')
    def click_transfer_funds(self):
        self.transfer_funds_option.click()

    @allure.step('Enter the amount to be transferred')
    def fill_transfer_amount_input(self, text: str):
        self.transfer_amount_input.send_keys(text)

    @allure.step('Click "From account #" dropdown')
    def click_from_account_dropdown(self):
        self.from_account_dropdown.click()

    @allure.step('Select "From account #" dropdown option')
    def select_from_account(self, account_id, dropdown_items):
        self.get_dropdown_item(account_id, dropdown_items).click()

    @allure.step('Click "to account #" dropdown')
    def click_to_account_dropdown(self):
        self.to_account_dropdown.click()

    @allure.step('Select "to account #" dropdown option')
    def select_to_account(self, account_id, dropdown_items):
        self.get_dropdown_item(account_id, dropdown_items).click()

    @allure.step('Click "Transfer" button')
    def click_transfer_button(self):
        self.transfer_button.click()

    def click_bill_pay_option(self):
        self.bill_pay_option.click()

    @allure.step('Enter Payee Name')
    def fill_payee_name_input(self, text: str):
        self.payee_name_input.send_keys(text)

    @allure.step('Enter Address')
    def fill_address_input(self, text: str):
        self.address_input.send_keys(text)

    @allure.step('Enter City')
    def fill_city_input(self, text: str):
        self.city_input.send_keys(text)

    @allure.step('Enter State')
    def fill_state_input(self, text: str):
        self.state_input.send_keys(text)

    @allure.step('Enter zip code')
    def fill_zip_code_input(self, text: str):
        self.zip_code_input.send_keys(text)

    @allure.step('Enter Phone')
    def fill_phone_input(self, text: str):
        self.phone_input.send_keys(text)

    @allure.step('Enter Account')
    def fill_account_input(self, text: str):
        self.account_input.send_keys(text)

    @allure.step('Enter Verify Account')
    def fill_verify_account_input(self, text: str):
        self.verify_account_input.send_keys(text)

    @allure.step('Enter Amount')
    def fill_amount_input(self, text: str):
        self.amount_input.send_keys(text)

    @allure.step('Click "From account #" dropdown')
    def click_from_account_dropdown_bill(self):
        self.from_account_id_dropdown.click()

    @allure.step('Click "Send Payment" button')
    def click_send_payment(self):
        self.send_payment_button.click()

    @allure.step('Click "Request Loan" option')
    def click_request_loan_option(self):
        self.request_loan_option.click()

    @allure.step('Enter Loan Amount')
    def fill_loan_amount_input(self, amount):
        self.loan_amount_input.send_keys(amount)

    @allure.step('Enter Down Payment')
    def fill_down_payment_input(self, amount):
        self.down_payment_input.send_keys(amount)

    @allure.step('Click "Apply now" button')
    def click_apply_now(self):
        self.apply_now_button.click()

    @allure.step('Click account ID')
    def navigate_to_account_activity(self, account_id):
        self.get_accounts_overview_account(account_id).click()


account_page = AccountPage()
