import json


def get_status_code(response):
    return response.status_code


def get_pretty_json(str_json):
    parsed = json.loads(str_json)
    return json.dumps(parsed, sort_keys=False, indent=2, separators=(",", ": "))
