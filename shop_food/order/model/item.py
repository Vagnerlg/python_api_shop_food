from typing import List

from pydantic import PositiveInt

from shop_food.infra.database.base_model import BaseModel
from shop_food.product.model.product import Product


class Item(BaseModel):
    product: Product
    quantity: PositiveInt

