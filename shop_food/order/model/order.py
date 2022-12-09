from typing import Optional, List

from shop_food.contracts.abstract_model import AbstractModel
from shop_food.order.model.address import Address
from shop_food.order.model.item import Item
from shop_food.order.model.status import Status
from shop_food.order.model.user import User


class Order(AbstractModel):
    user: User
    items: List[Item] = []
    status: Status
    address: Optional[Address]
