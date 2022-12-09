from typing import Any, Union


def response_success(data: Union[dict, list[Any]]) -> dict:
    return {
        'data': data
    }


def response_errors(data: Union[dict, list[Any]]) -> (dict, int):
    return {
        'errors': data
    }, 403
