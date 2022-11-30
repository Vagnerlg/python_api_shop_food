import pytest

from pydantic.error_wrappers import ValidationError

from shop_food.product.model.category import Category


def test_category():
    category = Category(**{
        'name': 'category name'
    })

    assert isinstance(category, Category)
    assert category.created_at is not None
    assert category.updated_at is not None
    assert category.name == 'category name'


def test_category_error():
    with pytest.raises(ValidationError) as error:
        Category()

    errors = error.value.errors()

    assert errors == [{
        'loc': ('name',),
        'msg': 'field required',
        'type': 'value_error.missing'
    }]
