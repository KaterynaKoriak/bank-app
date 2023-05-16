DEFAULT_BALANCE = 515.50
DEFAULT_MIN_BALANCE = 100.00
INITIALIZED_DB_FIRST_CUSTOMER_ID = 12212
INITIALIZED_DB_SECOND_CUSTOMER_ID = 12323
FIRST_REGISTERED_CUSTOMER_ID = 12434
CUSTOMER_ID_STEP_DB = 111
SUCCESS_CODE = 200
TEST_INITIAL_BALANCE = 1500.00
TEST_MIN_BALANCE = 150.00
BASIC_PASSWORD = "password"

test_messages = {'open_account_title': 'ParaBank | Open Account',
                 'transfer_funds_title': 'ParaBank | Transfer Funds',
                 'transfer_complete_title': 'Transfer Complete!',
                 'account_opened': 'Account Opened!',
                 'bill_payment_complete': 'Bill Payment Complete',
                 'minimal_amount_message': 'A minimum of ${:.2f} must be deposited into this account at time '
                                           'of opening. Please choose an existing account to transfer funds into '
                                           'the new account.'
                 }

account_types = {
    'CHECKING': 0,
    'SAVINGS': 1,
    'LOAN': 2
}