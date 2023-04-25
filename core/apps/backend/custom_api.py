import requests
import urllib3
from requests import Response

from core.testlib.helpers.api_decorators import api_logger, raise_error_on_request_fail

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class CustomApi:
    def __new__(cls, raise_exception_on_error: bool = True) -> object:
        instance = object.__new__(cls)
        if raise_exception_on_error:
            for attr in cls.__dict__:
                if callable(getattr(cls, attr)):
                    setattr(instance, attr, raise_error_on_request_fail(getattr(instance, attr)))
        return instance

    session = requests.session()
    url = ''
    api_key = {url: None}

    post_headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    get_headers = {
        "accept": "application/json",
    }

    @classmethod
    @api_logger
    def api_post_custom(cls, path: str, headers: dict = None, params: dict = None, data: dict = None,
                        json: dict = None, files: str = None, **kwargs) -> Response:
        if not headers:
            headers = cls.post_headers
        return cls.session.post(f'{cls.url}{path}', headers=headers, params=params, json=json, data=data,
                                files=files, **kwargs)

    @classmethod
    @api_logger
    def api_get_custom(cls, path: str, headers: dict = None, params: dict = None) -> Response:
        if not headers:
            headers = cls.get_headers
        return cls.session.get(f'{cls.url}{path}', headers=headers, params=params)
