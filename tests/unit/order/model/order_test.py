import pytest
from pydantic.error_wrappers import ValidationError

from shop_food.order.model.order import Order


def test_order():
    order = Order(**{
        'user': {
            'phone': '+5511989903623'
        },
        'items': [
            {
                'product': {
                    'title': 'pizza',
                    'short_description': 'mussarela',
                    'description': 'descrição de pizza com borda',
                    'price': 1523,
                    'category': {
                        'name': 'pizza'
                    }
                },
                'quantity': 1
            }
        ],
        'status': 'created'
    })

    assert isinstance(order, Order)


def test_order_error():
    with pytest.raises(ValidationError) as error:
        Order()

    errors = error.value.errors()

    assert errors == [
        {
            'loc': ('user',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('status',),
            'msg': 'field required',
            'type': 'value_error.missing'
        }
    ]
