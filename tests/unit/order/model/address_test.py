import pytest
from pydantic.error_wrappers import ValidationError

from shop_food.order.model.address import Address
from shop_food.order.model.item import Item


def test_address():
    pass
    # address = Address(**{
    #     'product': {
    #         'title': 'Titulo',
    #         'short_description': 'produto',
    #         'description': 'Produto com desconto',
    #         'price': 100,
    #         'category': {
    #             'name': 'categoria'
    #         }
    #     },
    #     'quantity': 1
    # })
    #
    # assert isinstance(address, Address)
    # assert address.created_at is not None
    # assert address.updated_at is not None


def test_address_error():
    with pytest.raises(ValidationError) as error:
        Address()

    errors = error.value.errors()

    assert errors == [
        {
            'loc': ('street',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('number',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('city',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('state',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('district',),
            'msg': 'field required',
            'type': 'value_error.missing'
        }
    ]

