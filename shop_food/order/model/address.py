from shop_food.contracts.abstract_model import AbstractModel
from typing import Optional


class Address(AbstractModel):
    street: str
    number: str
    city: str
    cep: Optional[str]
    state: str
    district: str
