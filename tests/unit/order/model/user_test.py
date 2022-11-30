import pytest
from pydantic.error_wrappers import ValidationError

from shop_food.order.model.user import User


def test_user():
    user = User(**{
        'email': 'email@email.com'
    })

    assert isinstance(user, User)
    assert user.created_at is not None
    assert user.updated_at is not None


def test_user_error():
    with pytest.raises(ValidationError) as error:
        User()

    errors = error.value.errors()

    assert errors == [{
        'loc': ('__root__',),
        'msg': 'user id not null phone, cpf and email',
        'type': 'value_error'
    }]
