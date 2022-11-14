from shop_food.infra.database.abstract_repository import AbstractRepository
from shop_food.infra.database.base_model import BaseModel
from shop_food.infra.database.relation import Relation
from shop_food.product.model.product import Product
from typing import List
from shop_food.product.repository.category_repository import CategoryRepository


class ProductRepository(AbstractRepository):
    collection: str = 'products'
    model = Product
    relation_one: List[Relation] = [
        Relation(field='category_id', model='category', repository=CategoryRepository)
    ]

    def all_products_by_category(self, id_cat: str) -> List[BaseModel]:
        return self.find({
            'category_id': id_cat
        })
