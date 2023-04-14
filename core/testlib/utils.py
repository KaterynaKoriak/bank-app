from faker import Faker

FAKE = Faker()


def get_random_str(n: int = 8) -> int:
    return FAKE.bothify(text='?' * n)


def get_random_int(min_value: int = 0, max_value: int = 9999) -> int:
    return FAKE.pyint(min_value, max_value)
