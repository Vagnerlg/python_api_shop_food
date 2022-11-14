from typing import List
from shop_food.infra.database.base_model import BaseModel
from shop_food.order.model.address import Address
from shop_food.order.model.status import Status
from shop_food.order.model.user import User
from shop_food.product.model.product import Product


class Order(BaseModel):
    id: str
    user: User
    items: List[Product] = []
    status: Status
    address: Address
