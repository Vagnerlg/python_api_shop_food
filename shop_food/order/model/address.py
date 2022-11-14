from shop_food.infra.database.base_model import BaseModel
from typing import Optional


class Address(BaseModel):
    street: str
    number: str
    city: str
    cep: Optional[str]
    state: str
    district: str
