from faker import Faker

FAKE = Faker()


def get_random_str(n: int = 8) -> int:
    return FAKE.bothify(text='?' * n)


def get_random_int(min_value: int = 0, max_value: int = 9999) -> int:
    return FAKE.pyint(min_value, max_value)


def get_random_street():
    return FAKE.street_address()


def get_random_first_name():
    return FAKE.first_name()


def get_random_last_name():
    return FAKE.last_name()


def get_random_city():
    return FAKE.city()


def get_random_state():
    return FAKE.state()


def get_random_zip_code():
    return FAKE.zipcode()


def get_random_phone_number():
    return FAKE.phone_number()


def get_random_ssn():
    return FAKE.ssn()


def get_random_password():
    return FAKE.password()
