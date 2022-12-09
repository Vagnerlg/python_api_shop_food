import pytest
from pydantic.error_wrappers import ValidationError

from shop_food.order.model.address import Address


def test_address():
    address = Address(**{
        'street': 'Av Paulista',
        'number': '1000',
        'city': 'São Paulo',
        'state': 'SP',
        'district': 'Centro'
    })

    assert isinstance(address, Address)
    assert address.created_at is not None
    assert address.updated_at is not None


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
