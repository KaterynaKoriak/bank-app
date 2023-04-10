from selene.support.shared import browser

from config.env import URL


class BasePage:
    path = ''

    def navigate(self):
        browser.driver.get(f'{URL}{self.path}')
