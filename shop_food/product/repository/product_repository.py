from shop_food.infra.database.abstract_repository import AbstractRepository
from shop_food.infra.database.base_model import BaseModel
from shop_food.product.model.product import Product
from typing import List


class ProductRepository(AbstractRepository):
    collection: str = 'products'
    model = Product

    def all_products_by_category(self, id_cat: str) -> List[BaseModel]:
        return self.find({
            'category_id': id_cat
        })
