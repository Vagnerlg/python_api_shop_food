from shop_food.infra.database.abstract_repository import AbstractRepository
from shop_food.product.model.category import Category


class CategoryRepository(AbstractRepository):
    collection: str = 'categories'
    model = Category
