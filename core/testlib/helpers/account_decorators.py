from functools import wraps

from core.apps.backend.ui_api import ui_api
from constants.variables import DEFAULT_BALANCE, DEFAULT_MIN_BALANCE


def register_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_data = kwargs["user_scenario"]
        ui_api.get_registration()
        ui_api.post_registration(user_data)
        result = func(*args, **kwargs)
        return result
    return wrapper


def edit_default_admin_values(initial_balance, min_balance):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ui_api.get_admin_page()
            ui_api.post_admin_changes(initial_balance=initial_balance, min_balance=min_balance)
            result = func(*args, **kwargs)
            ui_api.post_admin_changes(initial_balance=DEFAULT_BALANCE, min_balance=DEFAULT_MIN_BALANCE)
            return result
        return wrapper
    return my_decorator

