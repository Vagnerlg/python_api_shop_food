from datetime import datetime
from typing import Any


class Transform:

    def set_date(self, model: dict) -> None:
        model['updated_at'] = datetime.now()

    def merge(self, current: dict, new_model: dict) -> dict[str, Any]:
        if new_model.get('created_at'):
            del new_model['created_at']
        if new_model.get('updated_at'):
            del new_model['updated_at']
        self.set_date(current)

        prod_dict = current | new_model
        if prod_dict.get('id'):
            del prod_dict['id']

        return prod_dict

    def prepare_model(self, original: dict) -> dict:
        result = {}
        for key in original:
            if isinstance(original[key], dict):
                result[key] = self.prepare_model(original[key])
                continue

            if isinstance(original[key], list):
                items = []
                for item in original[key]:
                    if isinstance(item, dict):
                        items.append(self.prepare_model(item))
                        continue
                result[key] = items
                continue

            if original[key] is not None and key != '_id':
                result[key] = original[key]
                continue

            if '_id' == key:
                result['id'] = str(original[key])

        return result

    def prepare_obj(self, original: dict) -> dict:
        for key in original.copy():
            if isinstance(original[key], dict):
                if key in ['category', 'product']:
                    original[f'{key}_id'] = original[key]['id']
                    del original[key]
                    continue
                self.prepare_obj(original[key])
            if isinstance(original[key], list):
                items = []
                for item in original[key]:
                    if isinstance(item, dict):
                        items.append(self.prepare_obj(item))
                original[key] = items
        return original
