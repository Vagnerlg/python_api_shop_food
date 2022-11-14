from typing import List

from shop_food.infra.database.abstract_repository import AbstractRepository
from shop_food.infra.database.relation import Relation
from shop_food.infra.http.request.add_order_item import AddOrderItem
from shop_food.order.model.order import Order
from shop_food.order.repository.item_repository import ItemRepository


class OrderRepository(AbstractRepository):
    model = Order
    relation_many: List[Relation] = [
        Relation(field='items_id', model="items", repository=ItemRepository)
    ]

    def add_item(self, form_item: AddOrderItem) -> Order:
        # busca por pedido com status CREATED, se não encontra cria um
        # adiciona o produto e sua quantidade
        # retorna o Pedido
        ...
