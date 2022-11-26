from datetime import datetime

from shop_food.contracts.abstract_model import AbstractModel


def test_abstract_model():
    result = AbstractModel()

    assert isinstance(result.updated_at, datetime)
    assert isinstance(result.created_at, datetime)
