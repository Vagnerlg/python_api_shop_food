from typing import List

from shop_food.infra.database.abstract_repository import AbstractRepository
from shop_food.infra.database.relation import Relation
from shop_food.order.model.item import Item
from shop_food.product.repository.product_repository import ProductRepository


class ItemRepository(AbstractRepository):
    model = Item
    relation_one: List[Relation] = [
        Relation(field='id', model="product", repository=ProductRepository)
    ]
