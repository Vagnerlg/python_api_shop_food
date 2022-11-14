from typing import List
from pydantic import PositiveInt
from shop_food.infra.database.base_model import BaseModel
from shop_food.product.model.category import Category


class Product(BaseModel):
    title: str
    short_description: str
    description: str
    pictures: List[str] = []
    ingredients: List[str] = []
    category: Category
    price: PositiveInt

