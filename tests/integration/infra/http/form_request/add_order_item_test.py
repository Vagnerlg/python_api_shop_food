from pydantic.error_wrappers import ValidationError

from shop_food.infra.http.form_request.add_order_item import AddOrderItem
from tests.util.database import *


def test_form_add_order_item(product):

    add_order_item = AddOrderItem(**{
        'product_id': product.id,
        'user': {
            'type': 'phone',
            'value': 'sdasdasdasd'
        }
    })

    assert isinstance(add_order_item, AddOrderItem)
    assert isinstance(add_order_item.product, Product)
    assert add_order_item.product.id == product.id


def test_form_add_order_item_error():

    with pytest.raises(ValidationError) as error:
        AddOrderItem()

    errors = error.value.errors()

    assert errors == [
        {
            'loc': ('product_id',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('user',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('__root__',),
            'msg': 'product not found',
            'type': 'value_error'
        }
    ]
