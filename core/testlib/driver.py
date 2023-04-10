import tempfile

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from config.env import BROWSER, REMOTE_IP

browsers = {
    'chrome': webdriver.Chrome,
    'remote': webdriver.Remote
}


class Driver:
    def __init__(self, **kwargs) -> None:
        profile_dir = tempfile.mkdtemp()
        self.kwargs = kwargs
        if BROWSER == 'chrome':
            self.kwargs['executable_path'] = ChromeDriverManager().install()
            options = webdriver.ChromeOptions()
            options.add_argument("user-data-dir=" + profile_dir)
            options.add_argument("--start-maximized")
            # options.add_argument("--headless")  # Add this option to run in headless node
            self.kwargs['options'] = options
        if BROWSER == 'remote':
            self.kwargs['command_executor'] = f'http://{REMOTE_IP}:4444/wd/hub'
            self.kwargs['desired_capabilities'] = {
                "browserName": "chrome",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": False
                }
            }

    def start(self) -> WebDriver:
        return browsers[BROWSER](**self.kwargs)
