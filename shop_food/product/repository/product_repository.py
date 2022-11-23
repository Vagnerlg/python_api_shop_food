from pydantic.error_wrappers import ValidationError, ErrorWrapper
from shop_food.infra.database.abstract_repository import AbstractRepository
from shop_food.infra.database.base_model import BaseModel
from shop_food.product.model.product import Product
from typing import List

from shop_food.product.repository.category_repository import CategoryRepository


class ProductRepository(AbstractRepository):
    collection: str = 'products'
    model = Product

    def all_products_by_category(self, id_cat: str) -> List[BaseModel]:
        return self.find({
            'category_id': id_cat
        })

    def relations(self, model: dict) -> dict:
        category_id = model.get('category_id')
        category = CategoryRepository(self.db, self.transform).find_by_id(category_id)

        if not category:
            category = {
                'name': 'not found'
            }
        else:
            category = category.dict()

        model['category'] = category

        return self.transform.prepare_model(model)

    def validation_relations(self, model) -> None:
        category_id = model.get('category_id')
        if not category_id or not CategoryRepository(self.db, self.transform).find_by_id(category_id):
            raise ValidationError(
                model=self.model,
                errors=[
                    ErrorWrapper(loc='category', exc=Exception(f'category {category_id} not found'))
                ]
            )
