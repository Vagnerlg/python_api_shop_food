from enum import Enum
from typing import Optional

from pydantic import BaseModel, PositiveInt, root_validator

from shop_food.injector import boot_injector
from shop_food.product.model.product import Product
from shop_food.product.repository.product_repository import ProductRepository


class TypesUser(str, Enum):
    CPF = 'cpf'
    EMAIL = 'email'
    PHONE = 'phone'


class User(BaseModel):
    type: TypesUser
    value: str


class AddOrderItem(BaseModel):
    product_id: str
    product: Optional[Product]
    user: User
    quantity: PositiveInt = 1

    @root_validator
    def root_validate(cls, values):
        product_id = values.get('product_id')
        if product_id is None:
            raise ValueError('product not found')

        product = boot_injector().get(
            ProductRepository
        ).find_by_id(str(product_id))

        if product is None:
            raise ValueError('product not found')

        values['product'] = product

        return values
