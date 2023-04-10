from hamcrest import contains_string, assert_that, equal_to
from selene.support.shared import browser
from selene import query
from core.apps.frontend.pages.main_page import main_page


class MainPageSteps:
    @staticmethod
    def fill_form(first_name: str, last_name: str, address: str, city: str, state: str, zip_code: str, phone: str,
                  ssn: int, username: str, password: str) -> None:
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
        main_page.fill_confirm_input(password)
        main_page.click_register_button()


main_page_steps = MainPageSteps()


class MainPageAssertSteps:
    @staticmethod
    def check_welcome_username(username):
        print(f"this is username: {main_page.welcome_username.get(query.text)}")
        assert_that(main_page.welcome_username.get(query.text), equal_to(f'Welcome {username}'))

    @staticmethod
    def check_welcome_full_name(first_name, last_name):
        print(f"this is fullname: {main_page.welcome_user.get(query.text)}")
        assert_that(main_page.welcome_user.get(query.text), equal_to(f'Welcome {first_name} {last_name}'))

    @staticmethod
    def check_welcome_page_navigation(title):
        print(f"this is title: {main_page.welcome_page_title.get(query.text)}")
        assert_that(main_page.welcome_page_title.get(query.text), equal_to(title))


main_page_assert_steps = MainPageAssertSteps()
