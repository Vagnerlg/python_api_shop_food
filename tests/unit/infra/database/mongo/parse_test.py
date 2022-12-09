from datetime import datetime
import pytest

from shop_food.app import load_app
from bson import ObjectId

from shop_food.infra.database.mongo.parse import Transform


@pytest.fixture
def transform():
    fi = load_app('unit_testing')
    return fi.injector.get(Transform)


@pytest.fixture
def dict_object():
    return {
        'id': '6375a88f4f117d8c1d931b09',
        'created_at': datetime(2022, 11, 17, 0, 20, 47, 778000),
        'user': {
            'created_at': datetime(2022, 11, 17, 0, 20, 47, 778000),
            'email': 'vlgonalves@gmail.com'
        },
        'items': [
            {
                'created_at': datetime(2022, 11, 17, 0, 20, 47, 778000),
                'quantity': 1,
                'product': {
                    'id': '63724a1c7254bc2c84c02d76',
                    'created_at': datetime(2022, 11, 14, 11, 1, 0, 976000),
                    'title': 'Pizza Calabresa',
                    'category': {
                        'id': '636c72cf6ca49b5bd1234fa8',
                        'created_at': datetime(2022, 11, 10, 0, 41, 3, 190000),
                        'name': 'Pizzas'
                    }
                }
            }
        ],
        'status': 'created'
    }


@pytest.fixture
def dict_database():
    return {
        'id': '6375a88f4f117d8c1d931b09',
        'created_at': datetime(2022, 11, 17, 0, 20, 47, 778000),
        'user': {
            'created_at': datetime(2022, 11, 17, 0, 20, 47, 778000),
            'email': 'vlgonalves@gmail.com'
        },
        'items': [
            {
                'created_at': datetime(2022, 11, 17, 0, 20, 47, 778000),
                'quantity': 1,
                'product_id': '63724a1c7254bc2c84c02d76'
            }
        ],
        'status': 'created'
    }


def test_set_date(transform: Transform) -> None:
    result = {}
    transform.set_date(result)
    updated_at = result.get('updated_at')

    assert updated_at is not None
    assert isinstance(updated_at, datetime)


def test_merge_empty(transform: Transform) -> None:
    result = transform.merge({}, {})

    updated_at = result.get('updated_at')

    assert updated_at is not None
    assert isinstance(updated_at, datetime)


def test_merge_full(transform: Transform) -> None:
    result = transform.merge({
        'foo': 'foo',
        'field': 'old'
    }, {
        'bar': 'bar',
        'field': 'new'
    })

    expected = {
        'bar': 'bar',
        'field': 'new',
        'foo': 'foo'
    }

    del result['updated_at']

    assert expected == result


def test_prepare_obj(
        transform: Transform,
        dict_object: dict,
        dict_database: dict):
    result = transform.prepare_obj(dict_object)

    assert result == dict_database


def test_prepare_model(transform: Transform):
    result = transform.prepare_model({
        '_id': ObjectId('63724a1c7254bc2c84c02d76'),
        'other_dict': {
            '_id': ObjectId('63724a1c7254bc2c84c02d76'),
            'foo': True,
            'bar': None
        },
        'items': [
            {
                '_id': ObjectId('63724a1c7254bc2c84c02d76'),
                'bar': True
            },
            {
                '_id': ObjectId('63724a1c7254bc2c84c02d76'),
                'bar': False
            }
        ]
    })
    expected = {
        'id': '63724a1c7254bc2c84c02d76',
        'other_dict': {
            'id': '63724a1c7254bc2c84c02d76',
            'foo': True
        },
        'items': [
            {
                'id': '63724a1c7254bc2c84c02d76',
                'bar': True
            },
            {
                'id': '63724a1c7254bc2c84c02d76',
                'bar': False
            }
        ]
    }

    assert expected == result
