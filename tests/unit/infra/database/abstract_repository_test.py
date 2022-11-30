from datetime import datetime

from bson import ObjectId

from shop_food.contracts.abstract_model import AbstractModel
from shop_food.infra.database.abstract_repository import AbstractRepository
from tests.unit.infra.database.mongo.db import DB
from shop_food.infra.database.mongo.parse import Transform


def repository(expected: list[dict]):
    db = DB()
    db.expected(expected)
    repo = AbstractRepository(db, Transform())
    repo.model = AbstractModel
    repo.collection = 'foo_bar'

    return AbstractRepository(db, Transform())


def test_repo_find_by_id():

    # Set
    repo = repository([{
        'params': {
            'collection': 'foo_bar',
            'id_model': '1234'
        },
        'result': {
            '_id': ObjectId('63869e03ab8e42f4906ff16f'),
            'created_at': datetime(2022, 11, 29, 21, 4, 39, 47882),
            'updated_at': datetime(2022, 11, 29, 21, 4, 39, 47903)
        }
    }])
    expected = {
        'id': '63869e03ab8e42f4906ff16f',
        'created_at': datetime(2022, 11, 29, 21, 4, 39, 47882),
        'updated_at': datetime(2022, 11, 29, 21, 4, 39, 47903)
    }

    # Actions
    model = repo.find_by_id('1234')

    assert isinstance(model, AbstractModel)
    assert model.dict() == expected


def test_repo_all():

    # Set
    repo = repository([{
        'params': {
            'query': {}
        },
        'result': [{
            '_id': ObjectId('63869e03ab8e42f4906ff16f'),
            'created_at': datetime(2022, 11, 29, 21, 4, 39, 47882),
            'updated_at': datetime(2022, 11, 29, 21, 4, 39, 47903)
        }]
    }])
    expected = {
        'id': '63869e03ab8e42f4906ff16f',
        'created_at': datetime(2022, 11, 29, 21, 4, 39, 47882),
        'updated_at': datetime(2022, 11, 29, 21, 4, 39, 47903)
    }

    # Actions
    model = repo.all()

    assert isinstance(model, list)
    assert len(model) == 1
    assert isinstance(model[0], AbstractModel)
    assert model[0].dict() == expected


def test_repo_add():

    # Set
    repo = repository([
        {
            'params': {
                'collection': 'foo_bar',
                'data': {}
            },
            'result': {
                'inserted_id': ObjectId('63869e03ab8e42f4906ff16f')
            }
        },
        {
            'params': {
                'collection': 'foo_bar',
                'id_model': '63869e03ab8e42f4906ff16f'
            },
            'result': {
                '_id': ObjectId('63869e03ab8e42f4906ff16f'),
                'created_at': datetime(2022, 11, 29, 21, 4, 39, 47882),
                'updated_at': datetime(2022, 11, 29, 21, 4, 39, 47903)
            }
        }
    ])
    expected = {
        'id': '63869e03ab8e42f4906ff16f',
        'created_at': datetime(2022, 11, 29, 21, 4, 39, 47882),
        'updated_at': datetime(2022, 11, 29, 21, 4, 39, 47903)
    }

    # Actions
    model = repo.add(AbstractModel(**{}))

    assert isinstance(model, AbstractModel)
    assert model.dict() == expected


def test_repo_update():

    # Set
    repo = repository([
        {
            'params': {
                'collection': 'foo_bar',
                'id_model': '63869e03ab8e42f4906ff16f'
            },
            'result': {
                '_id': ObjectId('63869e03ab8e42f4906ff16f'),
                'created_at': datetime(2022, 11, 29, 21, 4, 39, 47882),
                'updated_at': datetime(2022, 11, 29, 21, 4, 39, 47903)
            }
        },
        {
            'params': {
                'id': '63869e03ab8e42f4906ff16f'
            },
        },
        {
            'params': {
                'collection': 'foo_bar',
                'id_model': '63869e03ab8e42f4906ff16f'
            },
            'result': {
                '_id': ObjectId('63869e03ab8e42f4906ff16f'),
                'created_at': datetime(2022, 11, 29, 21, 4, 39, 47882),
                'updated_at': datetime(2022, 11, 29, 21, 4, 39, 47903)
            }
        }
    ])
    expected = {
        'id': '63869e03ab8e42f4906ff16f',
        'created_at': datetime(2022, 11, 29, 21, 4, 39, 47882),
        'updated_at': datetime(2022, 11, 29, 21, 4, 39, 47903)
    }

    # Actions
    model = repo.update('63869e03ab8e42f4906ff16f', AbstractModel(**{}))

    assert isinstance(model, AbstractModel)
    assert model.dict() == expected


def test_repo_delete():

    # Set
    repo = repository([
        {
            'params': {
                'id': '63869e03ab8e42f4906ff16f'
            },
            'result': True
        }
    ])

    # Actions
    result = repo.delete('63869e03ab8e42f4906ff16f')

    assert result is True
