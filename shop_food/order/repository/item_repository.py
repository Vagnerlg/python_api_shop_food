from shop_food.infra.database.abstract_repository import AbstractRepository
from shop_food.order.model.item import Item


class ItemRepository(AbstractRepository):
    model = Item

