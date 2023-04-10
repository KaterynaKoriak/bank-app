from functools import wraps

from core.testlib.logger import LOGGER


def api_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        LOGGER.info(f'REQUEST: {result.request.method}: {result.request.url}')
        if result.request.method == 'POST' or result.request.method == 'PUT':
            LOGGER.info(f'REQUEST_DATA: {result.request.body}')
        LOGGER.info(f'CONTENT: {result.status_code}":" {result.content}')
        return result

    return wrapper


def raise_error_on_request_fail(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not result.ok:
            raise Exception(f'Error while api request: {result.status_code}":" {result.content}')

        return result

    return wrapper
