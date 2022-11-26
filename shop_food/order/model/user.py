from shop_food.contracts.abstract_model import AbstractModel
from pydantic import root_validator
from typing import Optional


class User(AbstractModel):
    phone: Optional[str]
    cpf: Optional[str]
    email: Optional[str]

    @root_validator
    def check_passwords_match(cls, values):
        phone, cpf, email = values.get('phone'), values.get('cpf'), values.get('email')
        if phone is None and cpf is None and email is None:
            raise ValueError('user id not null phone, cpf and email')
        return values
