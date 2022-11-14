from shop_food.infra.database.base_model import BaseModel
from typing import Optional


class User(BaseModel):
    phone: Optional[str]
    cpf: Optional[str]
    email: Optional[str]
