from typing import List
from shop_food.infra.database.base_model import BaseModel


class Product(BaseModel):
    title: str
    short_description: str
    description: str
    pictures: List[str] = []
    ingredients: List[str] = []
    #category
