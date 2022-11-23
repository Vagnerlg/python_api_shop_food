from typing import Optional, List

from bson import ObjectId
from injector import inject

from shop_food.infra.database.base_model import BaseModel
from shop_food.infra.database.db import DB
from shop_food.infra.database.util.parse import Transform


class AbstractRepository:
    model = BaseModel
    collection: str = ''
    transform: Transform

    @inject
    def __init__(self, db: DB, transform: Transform):
        self.db = db
        self.transform = transform

    def get_db(self):
        return self.db.get_collection(self.collection)

    def all(self):
        items = []
        for item in self.get_db().find():
            items.append(self.model(** self.relations(item)))

        return items

    def find_by_id(self, id_model: str) -> Optional[BaseModel]:
        result = self.get_db().find_one({
            '_id': ObjectId(id_model)
        })

        if not result:
            return None

        return self.model(**self.relations(result))

    def add(self, model: BaseModel) -> BaseModel:
        item_dict = self.transform.prepare_obj(model.dict())
        self.validation_relations(item_dict)
        result = self.get_db().insert_one(item_dict)

        return self.find_by_id(str(result.inserted_id))

    def update(self, id_model: str, prod: BaseModel) -> Optional[BaseModel]:
        actual = self.find_by_id(id_model)
        if not actual:
            return None

        self.validation_relations(prod.dict())
        prod_dict = self.transform.merge(
            self.transform.prepare_obj(actual.dict()),
            self.transform.prepare_obj(prod.dict())
        )
        self.get_db().update_one({
            '_id': ObjectId(id_model)
        }, {
            '$set': prod_dict
        })

        return self.find_by_id(id_model)

    def delete(self, id_model: str) -> bool:
        result = self.get_db().delete_one({
            '_id': ObjectId(id_model)
        })
        if 0 < result.deleted_count.bit_count():
            return True
        return False

    def find(self, query: dict) -> List[BaseModel]:
        result = self.get_db().find(query)
        items = []
        for item in result:
            items.append(self.model(** self.relations(item)))

        return items

    def relations(self, model: dict) -> dict:
        return self.transform.prepare_model(model)

    def validation_relations(self, model) -> None:
        ...
