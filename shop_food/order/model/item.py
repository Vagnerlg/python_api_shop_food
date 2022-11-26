from pydantic import PositiveInt

from shop_food.contracts.abstract_model import AbstractModel
from shop_food.product.model.product import Product


class Item(AbstractModel):
    product: Product
    quantity: PositiveInt

