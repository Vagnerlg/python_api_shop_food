import pytest
from pydantic.error_wrappers import ValidationError

from shop_food.product.model.product import Product


def test_product():
    product = Product(**{
        'title': 'Titulo',
        'short_description': 'produto',
        'description': 'Produto com desconto',
        'price': 100,
        'category': {
            'name': 'categoria'
        }
    })

    assert isinstance(product, Product)


def test_product_error():
    with pytest.raises(ValidationError) as error:
        Product()

    errors = error.value.errors()

    assert errors == [
        {
            'loc': ('title',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('short_description',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('description',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('category',),
            'msg': 'field required',
            'type': 'value_error.missing'
        },
        {
            'loc': ('price',),
            'msg': 'field required',
            'type': 'value_error.missing'
        }
    ]
