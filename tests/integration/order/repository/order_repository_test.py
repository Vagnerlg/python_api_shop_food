from shop_food.infra.http.form_request.add_order_item import AddOrderItem


def test_not_found(order_repository):
    result = order_repository.find_by_id('6394f958beb9f0ed4c88439c')

    assert result is None


def test_find_by_id(order_repository, order):
    result = order_repository.find_by_id(order.id)

    assert result.id == order.id
    assert result.created_at is not None
    assert result.updated_at is not None


def test_find_all(order_repository, order):
    result = order_repository.all()

    assert len(result) == 1
    assert result[0].id is not None


def test_add_item(order_repository, product):
    form_order = AddOrderItem(
        product_id=product.id,
        user={
            'type': 'email',
            'value': 'email@email.com'
        }
    )
    result = order_repository.add_item(form_order)

    assert result.id is not None
    assert len(result.items) == 1


def test_add_item_with_order_exists(order_repository, product):
    form_order = AddOrderItem(
        product_id=product.id,
        user={
            'type': 'email',
            'value': 'email@email.com'
        }
    )
    order = order_repository.add_item(form_order)
    result = order_repository.add_item(form_order)

    assert result.id is not None
    assert result.id == order.id
    assert len(order.items) == 1
    assert len(result.items) == 2
