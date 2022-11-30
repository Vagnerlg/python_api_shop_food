import pytest
from pymongo import MongoClient

from shop_food.injector import boot_injector
from shop_food.integration_config import IntegrationConfig
from shop_food.product.model.category import Category
from shop_food.product.model.product import Product
from shop_food.product.repository.category_repository import CategoryRepository
from shop_food.product.repository.product_repository import ProductRepository


@pytest.fixture(autouse=True)
def clear_database():
    config = IntegrationConfig()
    db_config = config.DATABASE.get('mongodb')
    client = MongoClient(
        'mongodb://' +
        db_config['user'] + ':' +
        db_config['password'] + '@' +
        db_config['url'] + ':' +
        str(db_config['port']) + '/'
    )
    client.drop_database(db_config['name'])
    print('clear_database')


@pytest.fixture()
def categoryRepository():
    return boot_injector().get(CategoryRepository)


@pytest.fixture()
def category(categoryRepository):
    return categoryRepository.add(Category(**{
        'name': 'Pizza'
    }))


@pytest.fixture()
def productRepository():
    return boot_injector().get(ProductRepository)


@pytest.fixture()
def product(productRepository, category):
    return productRepository.add(Product(**{
        'title': 'Pizza Mussarela',
        'short_description': 'Saborosa',
        'description': 'imperdivel',
        'price': 1000,
        'category': category.dict()
    }))
