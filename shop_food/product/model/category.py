from typing import Optional
from shop_food.infra.database.base_model import BaseModel


class Category(BaseModel):
    id: Optional[str]
    name: str
