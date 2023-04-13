from hamcrest import assert_that, equal_to
from selene.support.shared import browser
from core.apps.frontend.pages.main_page import main_page


class MainPageSteps:
    @staticmethod
    def fill_form(first_name: str, last_name: str, address: str, city: str, state: str, zip_code: str, phone: str,
                  ssn: int, username: str, password: str, confirmation_password: str) -> None:
        main_page.click_register_link()
        main_page.fill_first_name_input(first_name)
        main_page.fill_last_name_input(last_name)
        main_page.fill_address_input(address)
        main_page.fill_city_input(city)
        main_page.fill_state_input(state)
        main_page.fill_zip_code_input(zip_code)
        main_page.fill_phone_input(phone)
        main_page.fill_ssn_input(ssn)
        main_page.fill_username_input(username)
        main_page.fill_password_input(password)
        main_page.fill_confirm_input(confirmation_password)
        main_page.click_register_button()


main_page_steps = MainPageSteps()


class MainPageAssertSteps:
    @staticmethod
    def check_welcome_username(username):
        assert_that(main_page.welcome_username().text, equal_to(f'Welcome {username}'))

    @staticmethod
    def check_welcome_full_name(first_name, last_name):
        assert_that(main_page.welcome_user().text, equal_to(f'Welcome {first_name} {last_name}'))

    @staticmethod
    def check_welcome_page_navigation(title):
        assert_that(main_page.welcome_page_title().get_attribute("innerHTML"), equal_to(title))

    @staticmethod
    def check_existing_username_error_message(error_message):
        assert_that(main_page.error_existing_username().text, equal_to(error_message))

    @staticmethod
    def check_empty_password_error_message(error_message):
        assert_that(main_page.required_password_error().text, equal_to(error_message))

    @staticmethod
    def check_confirm_password_error_message(error_message):
        assert_that(main_page.password_confirmation_error().text, equal_to(error_message))


main_page_assert_steps = MainPageAssertSteps()
