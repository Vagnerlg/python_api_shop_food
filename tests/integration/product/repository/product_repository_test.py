from shop_food.product.model.product import Product


def test_not_found(product_repository):
    result = product_repository.find_by_id('6394f958beb9f0ed4c88439c')

    assert result is None


def test_find_by_id(product_repository, product):
    result = product_repository.find_by_id(product.id)

    assert result.id == product.id
    assert result.created_at is not None
    assert result.updated_at is not None


def test_find_all(product_repository, product):
    result = product_repository.all()

    assert len(result) == 1
    assert result[0].id is not None


def test_add_basic(product_repository, category):
    result = product_repository.add(Product(
        title='Pizza Mussarela',
        short_description='Super Saborosa',
        description='Massa perfeita com ingredientes selecionados',
        category={
            'id': category.id,
            'name': category.name
        },
        price=100
    ))

    assert result.id is not None
    assert result.created_at is not None
    assert result.updated_at is not None
    assert result.title == 'Pizza Mussarela'


def test_add_full(product_repository, category):
    result = product_repository.add(Product(
        title='Pizza Mussarela',
        short_description='Super Saborosa',
        description='Massa perfeita com ingredientes selecionados',
        category={
            'id': category.id,
            'name': category.name
        },
        price=100,
        pictures=['url/photo_1', 'url/photo_2'],
        ingredients=['tomate', 'mussarela']
    ))

    assert result.id is not None
    assert result.created_at is not None
    assert result.updated_at is not None
    assert result.title == 'Pizza Mussarela'
    assert result.pictures == ['url/photo_1', 'url/photo_2']
    assert result.ingredients == ['tomate', 'mussarela']


def test_update(product_repository, product):
    result = product_repository.update(product.id, Product(
        title='Pizza Mussarela 2',
        short_description='Super Saborosa',
        description='Massa perfeita com ingredientes selecionados',
        category={
            'id': product.category.id,
            'name': product.category.name
        },
        price=100,
        pictures=['url/photo_1', 'url/photo_2'],
        ingredients=['tomate', 'mussarela', 'azeitona']
    ))

    assert result.id is not None
    assert result.created_at is not None
    assert result.updated_at is not None
    assert result.title == 'Pizza Mussarela 2'
    assert result.pictures == ['url/photo_1', 'url/photo_2']
    assert result.ingredients == ['tomate', 'mussarela', 'azeitona']


def test_delete(product_repository, product):
    first = product_repository.find_by_id(product.id)
    product_repository.delete(product.id)
    result = product_repository.find_by_id(product.id)

    assert first is not None
    assert result is None


def test_all_products_by_category_empty(product_repository):
    result = product_repository.all_products_by_category(
        '6394f958beb9f0ed4c88439c'
    )

    assert result == []


def test_all_products_by_category(product_repository, product):
    result = product_repository.all_products_by_category(product.category.id)

    assert len(result) == 1
    assert result[0].category.id == product.category.id
