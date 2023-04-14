import allure
from hamcrest import equal_to
from core.testlib.matchers import check_that
from selene.support.shared import browser
from core.apps.frontend.pages.main_page import main_page


class MainPageSteps:
    @allure.step('Fill in the registration form')
    def fill_form(self, userdata) -> None:
        main_page.click_register_link()
        main_page.fill_first_name_input(userdata.first_name)
        main_page.fill_last_name_input(userdata.last_name)
        main_page.fill_address_input(userdata.address)
        main_page.fill_city_input(userdata.city)
        main_page.fill_state_input(userdata.state)
        main_page.fill_zip_code_input(userdata.zip_code)
        main_page.fill_phone_input(userdata.phone)
        main_page.fill_ssn_input(userdata.ssn)
        main_page.fill_username_input(userdata.username)
        main_page.fill_password_input(userdata.password)
        main_page.fill_confirm_input(userdata.confirmation_password)
        main_page.click_register_button()


main_page_steps = MainPageSteps()


class MainPageAssertSteps:
    @allure.step('Check welcome username message')
    def check_welcome_username(self, username):
        check_that(main_page.welcome_username().text, equal_to(f'Welcome {username}'),
                   f'"Welcome {username}" message is displayed')

    @allure.step('Check welcome first and last name message')
    def check_welcome_full_name(self, first_name, last_name):
        check_that(main_page.welcome_user().text, equal_to(f'Welcome {first_name} {last_name}'),
                   f'"Welcome {first_name} {last_name}" message is displayed')

    @allure.step('Check page title')
    def check_welcome_page_navigation(self, title):
        check_that(main_page.welcome_page_title().get_attribute("innerHTML"), equal_to(title),
                   f'page title is "{title}"')

    @allure.step('Check form with existing username')
    def check_existing_username_error_message(self, error_message):
        check_that(main_page.error_existing_username().text, equal_to(error_message),
                   f'"{error_message}" is displayed when submitting form with existing username')

    @allure.step('Check form with empty password field')
    def check_empty_password_error_message(self, error_message):
        check_that(main_page.required_password_error().text, equal_to(error_message),
                   f'"{error_message}" is displayed when submitting form with empty password')

    @allure.step('Check confirm password error message')
    def check_confirm_password_error_message(self, error_message):
        check_that(main_page.password_confirmation_error().text, equal_to(error_message),
                   f'"{error_message}" is displayed when submitting form with invalid confirm password')


main_page_assert_steps = MainPageAssertSteps()
