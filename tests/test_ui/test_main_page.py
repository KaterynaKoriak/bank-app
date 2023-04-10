import allure
import pytest

from steps.ui_steps.main_page_steps import main_page_steps, main_page_assert_steps


testdata = [('kkk','test','1234 Daisy Street','Cincinnati','Ohio',12345,1234567890,987654321,'kkk_ttestt','password')]
title = "ParaBank | Customer Created"


@allure.description('RGU-1')
@allure.title('Create user')
@allure.tag('Main Page')
@pytest.mark.parametrize("first_name,last_name,address,city,state,zip_code,phone,ssn,username,password", testdata)
@pytest.mark.usefixtures('driver')
def test_registration(first_name, last_name, address, city, state, zip_code, phone, ssn, username, password):
    main_page_steps.fill_form(first_name, last_name, address, city, state, zip_code, phone, ssn, username, password)
    main_page_assert_steps.check_welcome_username(username)
    main_page_assert_steps.check_welcome_full_name(first_name, last_name)
    main_page_assert_steps.check_welcome_page_navigation(title)
