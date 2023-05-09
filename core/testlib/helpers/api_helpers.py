import json


def get_status_code(response):
    return response.status_code


def get_pretty_json(str_json):
    parsed = json.loads(str_json)
    return json.dumps(parsed, sort_keys=False, indent=2, separators=(",", ": "))


def format_two_digits_after_comma(digit):
    formatted_digit = "{:.2f}".format(digit)
    return formatted_digit

