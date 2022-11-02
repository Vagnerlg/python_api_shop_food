from .model import Product
from .repository import Repository
from flask import request
from pydantic import ValidationError
from shop_food.infra.http.response import response_errors, response_success


def products():
    prods = Repository().all()
    return response_success([prod.dict() for prod in prods])


def product(id_prod: str):
    prod = Repository().find_by_id(id_prod)
    if None == prod:
        return response_errors({
                'product': 'not_found'
            })

    return response_success(prod.dict())


def add_product():
    try:
        prod = Product(** request.get_json())
        result = Repository().add(prod)
        return response_success(result.dict())
    except ValidationError as e:
        return response_errors(e.errors())


def update_product(id_prod: str):
    try:
        prod = Product(** request.get_json())
        result = Repository().update(id_prod, prod)
        return response_success(result.dict())
    except ValidationError as e:
        return response_errors(e.errors())


def delete_product(id_prod: str):
    try:
        result = Repository().delete(id_prod)
        if result:
            return response_success({
                'delete': True
            })
        return response_errors({
                'delete': False
            })
    except ValidationError as e:
        return response_errors(e.errors())
