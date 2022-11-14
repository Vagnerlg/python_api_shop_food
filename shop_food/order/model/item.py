from pydantic import BaseModel, PositiveInt

from shop_food.product.model.product import Product


class Item(BaseModel):
    product: Product
    quantity: PositiveInt
