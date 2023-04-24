import os
from dotenv import load_dotenv

load_dotenv()  # load sys vars from .env file


def get(key: str, default: any = None):
    return os.environ.get(key=key, default=default)


URL = get('URL', 'http://localhost:8080/parabank')
API_URL = get('URL', 'http://localhost:8080/parabank/services/bank')
BROWSER = get('BROWSER', 'chrome')
REMOTE_IP = get('REMOTE_IP', 'localhost')
