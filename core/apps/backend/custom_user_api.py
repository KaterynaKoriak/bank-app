# import allure
# from requests import Response
# from addict import Dict
# from config.env import URL
# from core.apps.backend.custom_api import CustomApi
#
#
# class UserApi(CustomApi):
#     url = URL
#
#     @allure.step("Register new customer")
#     def register_new_customer(self, user_data: Dict) -> Response:
#         self.api_get_custom("/register.htm")
#         data = {
#             'customer.firstName': user_data.customer.firstName,
#             'customer.lastName': user_data.customer.lastName,
#             'customer.address.street': user_data.customer.address.street,
#             'customer.address.city': user_data.customer.address.city,
#             'customer.address.state': user_data.customer.address.state,
#             'customer.address.zipCode': user_data.customer.address.zipCode,
#             'customer.phoneNumber': user_data.customer.phoneNumber,
#             'customer.ssn': user_data.customer.ssn,
#             'customer.username': user_data.customer.username,
#             'customer.password': user_data.customer.password,
#             'repeatedPassword': user_data.repeatedPassword
#         }
#         headers = {
#             "Content-Type": "application/x-www-form-urlencoded"
#         }
#         return self.api_post_custom(f'/register.htm', data=data, headers=headers)
#
#
# user_api = UserApi()
