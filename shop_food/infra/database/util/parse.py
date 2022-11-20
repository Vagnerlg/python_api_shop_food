from datetime import datetime
from typing import Any

from bson import ObjectId

from shop_food.config import DevConfig
from shop_food.infra.database.db import DB

collections = {
    'category': 'categories',
    'product': 'products'
}

config_db = DevConfig().DATABASE.get('mongodb')


def set_date(model: dict) -> None:
    model['updated_at'] = datetime.now()


def merge(current: dict, new_model: dict) -> dict[str, Any]:
    del new_model['created_at']
    del new_model['updated_at']
    set_date(current)

    prod_dict = current | new_model
    del prod_dict['id']

    return prod_dict


def find_id(key: str, value: str) -> dict:
    result = DB(config_db).get_collection(collections[key]).find_one({
        '_id': ObjectId(value)
    })

    if not result:
        return DB(config_db).get_collection(collections[key]).find_one()

    return result


def prepare_model(original: dict) -> dict:
    result = {}
    for key in original:
        if isinstance(original[key], dict):
            result[key] = prepare_model(original[key])
            continue

        if isinstance(original[key], list):
            items = []
            for item in original[key]:
                if isinstance(item, dict):
                    items.append(prepare_model(item))
                    continue
            result[key] = items
            continue

        if '_id' in key and key != '_id':
            key_model = key.replace('_id', '')
            result[key_model] = prepare_model(find_id(key_model, original[key]))
            continue

        if original[key] and key != '_id':
            result[key] = original[key]
            continue

        if '_id' == key:
            result['id'] = str(original[key])

    return result


def verify_relation(model: str) -> bool:
    return bool(collections.get(model))


def prepare_obj(original: dict) -> dict:
    for key in original.copy():
        if isinstance(original[key], dict):
            if verify_relation(key):
                original[f'{key}_id'] = original[key]['id']
                del original[key]
                continue
            prepare_obj(original[key])
        if isinstance(original[key], list):
            items = []
            for item in original[key]:
                if isinstance(item, dict):
                    items.append(prepare_obj(item))
            original[key] = items
    return original
