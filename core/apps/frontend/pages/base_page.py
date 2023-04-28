from selene.support.shared import browser

from config.env import BASE_URL


class BasePage:
    path = ''

    def navigate(self):
        browser.driver.get(f'{BASE_URL}{self.path}')
