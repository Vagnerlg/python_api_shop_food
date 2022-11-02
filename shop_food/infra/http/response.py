from typing import Any, Union


def response_success(data: Union[dict[str, Any], list[Any]]) -> dict[str, Any]:
    return {
        'data': data
    }


def response_errors(data: Union[dict[str, Any], list[Any]]) -> (dict[str, Any], int):
    return {
        'errors': data
    }, 403
