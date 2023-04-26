from selene.support.shared import browser

from config.env import API_URL


class BasePage:
    path = ''

    def navigate(self):
        browser.driver.get(f'{API_URL}{self.path}')
