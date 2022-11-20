from typing import Optional, List

from shop_food.infra.database.base_model import BaseModel
from shop_food.order.model.address import Address
from shop_food.order.model.item import Item
from shop_food.order.model.status import Status
from shop_food.order.model.user import User


class Order(BaseModel):
    user: User
    items: List[Item] = []
    status: Status
    address: Optional[Address]

