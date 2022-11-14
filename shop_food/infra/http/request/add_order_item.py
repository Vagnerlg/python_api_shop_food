from enum import Enum

from pydantic import BaseModel, PositiveInt


class TypesUser(str, Enum):
    CPF = 'cpf'
    EMAIL = 'email'
    PHONE = 'phone'


class User(BaseModel):
    type: TypesUser
    value: str


class AddOrderItem(BaseModel):
    product_id: str
    user: User
    quantity: PositiveInt
