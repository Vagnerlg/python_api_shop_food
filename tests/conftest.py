import os

import pytest
from pymongo import MongoClient

from shop_food.infra.http.form_request.add_order_item import AddOrderItem
from shop_food.injector import boot_injector
from shop_food.integration_config import IntegrationConfig
from shop_food.order.repository.order_repository import OrderRepository
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


@pytest.fixture()
def boot():
    os.environ['ENV'] = 'integration_testing'
    return boot_injector()


@pytest.fixture()
def category_repository(boot):
    return boot.get(CategoryRepository)


@pytest.fixture()
def category(category_repository):
    return category_repository.add(Category(**{
        'name': 'Pizza'
    }))


@pytest.fixture()
def product_repository(boot):
    return boot.get(ProductRepository)


@pytest.fixture()
def product(product_repository, category):
    return product_repository.add(Product(**{
        'title': 'Pizza Mussarela',
        'short_description': 'Saborosa',
        'description': 'imperdivel',
        'price': 1000,
        'category': category.dict()
    }))


@pytest.fixture()
def order_repository(boot):
    return boot.get(OrderRepository)


@pytest.fixture()
def order(order_repository, product):
    form_order = AddOrderItem(
        product_id=product.id,
        user={
            'type': 'email',
            'value': 'email@email.com'
        }
    )

    return order_repository.add_item(form_order)
