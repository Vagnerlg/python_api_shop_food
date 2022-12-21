import os

from shop_food.product.repository.category_repository import CategoryRepository
from shop_food.product.repository.product_repository import ProductRepository


class Config(object):
    APP_NAME = 'shop_food'
    REPOSITORIES = {
        'category': CategoryRepository,
        'product': ProductRepository
    }

    def database(self) -> dict:
        return {
            'mongodb': {
                'drive': os.getenv('DB_DRIVE', 'mongodb'),
                'user': os.getenv('DB_USER', 'root'),
                'password': os.getenv('DB_PASSWORD', 'example'),
                'url': os.getenv('DB_URL', 'localhost'),
                'port': 27017,
                'name': os.getenv('DB_NAME', 'shop-food')
            }
        }
