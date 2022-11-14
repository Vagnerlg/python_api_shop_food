from datetime import datetime
from typing import List, Any

from shop_food.infra.database.base_model import BaseModel
from shop_food.infra.database.db import DB
from shop_food.infra.database.relation import Relation


class UtilModel(DB):
    relations: List[Relation] = []

    def set_date(self, model: BaseModel) -> None:
        if None == model.created_at:
            model.created_at = datetime.now()
        model.updated_at = datetime.now()

    def embed(self, model_dict: dict) -> dict:
        for relation in self.relations:
            model_dict[relation.model] = relation.repository().find_by_id(
                model_dict[relation.field]).dict()

        return model_dict

    def relations_obj(self, model: BaseModel) -> dict:
        model_dict = model.dict()
        for relation in self.relations:
            model_dict[relation.field] = model_dict[relation.model][relation.model_id]
            del model_dict[relation.model]

        return model_dict

    def merge(self, current: BaseModel, actual: BaseModel) -> dict[str, Any]:
        new_model = actual.dict()
        del new_model['created_at']
        del new_model['updated_at']
        self.set_date(current)
        prod_dict = current.dict() | new_model
        del prod_dict['id']

        return prod_dict
