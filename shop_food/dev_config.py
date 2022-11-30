from shop_food.product.repository.category_repository import CategoryRepository
from shop_food.product.repository.product_repository import ProductRepository


class DevConfig(object):
    APP_NAME = 'shop_food'
    DATABASE = {
        'default': 'mongodb',
        'mongodb': {
            'drive': 'mongodb',
            'user': 'root',
            'password': 'example',
            'url': 'localhost',
            'port': 27017,
            'name': 'shop-food'
        }
    }
    REPOSITORIES = {
        'category': CategoryRepository,
        'product': ProductRepository
    }
