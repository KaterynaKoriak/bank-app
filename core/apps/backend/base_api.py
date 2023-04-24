import requests
import urllib3
from requests import Response

from core.testlib.helpers.api_decorators import api_logger, raise_error_on_request_fail

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class BaseApi:
    def __new__(cls, raise_exception_on_error: bool = True) -> object:
        """
        This wrapper provide option to create 'strict' or 'soft' API instances
        with a raise_exception_on_error=False flag, exception will be raised in case of result!=ok
        in case of raise_exception_on_error=True - it will be processed silently to make negative testing possible
        """
        instance = object.__new__(cls)
        if raise_exception_on_error:
            for attr in cls.__dict__:
                if callable(getattr(cls, attr)):
                    setattr(instance, attr, raise_error_on_request_fail(getattr(instance, attr)))
        return instance

    session = requests.session()
    api_url = ''
    url = ''
    api_key = {api_url: None}  # it's possible to share apikey between all child's when get it once or
    # use different keys for different services

    post_headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    get_headers = {
        "accept": "application/json",
    }

    @classmethod
    @api_logger
    def api_get(cls, path: str, headers: dict = None, params: dict = None) -> Response:
        if not headers:
            headers = cls.get_headers
        return cls.session.get(f'{cls.api_url}{path}', headers=headers, params=params)

    @classmethod
    @api_logger
    def api_patch(cls, path: str, headers: dict = None, data: dict = None, json: dict = None,
                  params: dict = None) -> Response:
        if not headers:
            headers = cls.post_headers
        return cls.session.patch(f'{cls.api_url}{path}', headers=headers, params=params, data=data, json=json)

    @classmethod
    @api_logger
    def api_post(cls, path: str, headers: dict = None, params: dict = None, data: dict = None, json: dict = None,
                 files: str = None, **kwargs) -> Response:
        if not headers:
            headers = cls.post_headers
        return cls.session.post(f'{cls.api_url}{path}', headers=headers, params=params, json=json, data=data,
                                files=files, **kwargs)

    @classmethod
    @api_logger
    def api_post_from_ui(cls, path: str, headers: dict = None, params: dict = None, data: dict = None,
                         json: dict = None, files: str = None, **kwargs) -> Response:
        if not headers:
            headers = cls.post_headers
        return cls.session.post(f'{cls.url}{path}', headers=headers, params=params, json=json, data=data,
                                files=files, **kwargs)


    @classmethod
    @api_logger
    def api_delete(cls, path: str, headers: dict = None, params: dict = None) -> Response:
        if not headers:
            headers = cls.post_headers
        return cls.session.delete(f'{cls.api_url}{path}', headers=headers, params=params)

    @classmethod
    @api_logger
    def api_put(cls, path: str, headers: dict = None, params: dict = None, json=None) -> Response:
        if not headers:
            headers = cls.post_headers
        return cls.session.put(f'{cls.api_url}{path}', headers=headers, data=params, json=json)
