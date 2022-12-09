import pytest
from pydantic.error_wrappers import ValidationError

from shop_food.order.model.item import Item


def test_user():
    item = Item(**{
        'product': {
            'title': 'Titulo',
            'short_description': 'produto',
            'description': 'Produto com desconto',
            'price': 100,
            'category': {
                'name': 'categoria'
            }
        },
        'quantity': 1
    })

    assert isinstance(item, Item)
    assert item.created_at is not None
    assert item.updated_at is not None


def test_user_error():
    with pytest.raises(ValidationError) as error:
        Item()

    errors = error.value.errors()

    assert errors == [
        {
            'loc': ('product',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('quantity',),
            'msg': 'field required',
            'type': 'value_error.missing'
        }
    ]
