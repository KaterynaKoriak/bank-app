import json


def get_status_code(response):
    return response.status_code


def get_text_from_json(str_json):
    return json.loads(str_json.text)


def format_two_digits_after_comma(digit):
    formatted_digit = "{:.2f}".format(digit)
    return formatted_digit

