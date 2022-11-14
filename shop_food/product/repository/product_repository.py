from shop_food.infra.database.abstract_repository import AbstractRepository
from shop_food.infra.database.relation import Relation
from shop_food.product.model.product import Product
from typing import List
from shop_food.product.repository.category_repository import CategoryRepository


class ProductRepository(AbstractRepository):
    collection: str = 'products'
    model = Product
    relations: List[Relation] = [
        Relation(field='category_id', model='category', repository=CategoryRepository)
    ]
