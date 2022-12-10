from shop_food.product.model.category import Category


def test_not_found(category_repository):
    result = category_repository.find_by_id('6394f958beb9f0ed4c88439c')

    assert result is None


def test_find_id(category_repository, category):
    result = category_repository.find_by_id(category.id)

    assert result.id == category.id
    assert result.created_at is not None
    assert result.updated_at is not None


def test_find_all(category_repository, category):
    result = category_repository.all()

    assert len(result) == 1
    assert result[0].id is not None


def test_add(category_repository):
    result = category_repository.add(Category(name='Pizza'))

    assert result.id is not None
    assert result.created_at is not None
    assert result.updated_at is not None
    assert result.name == 'Pizza'


def test_update(category_repository, category):
    old_name = category.name
    category.name = 'Esfiha'
    result = category_repository.update(category.id, category)
    print(result)
    assert category.name != old_name
    assert category.name == 'Esfiha'


def test_delete(category_repository, category):
    first = category_repository.find_by_id(category.id)
    category_repository.delete(category.id)
    result = category_repository.find_by_id(category.id)

    assert first is not None
    assert result is None
