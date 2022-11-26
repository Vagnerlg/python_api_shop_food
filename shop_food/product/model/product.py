from typing import List
from pydantic import PositiveInt
from shop_food.contracts.abstract_model import AbstractModel
from shop_food.product.model.category import Category


class Product(AbstractModel):
    title: str
    short_description: str
    description: str
    pictures: List[str] = []
    ingredients: List[str] = []
    category: Category
    price: PositiveInt
