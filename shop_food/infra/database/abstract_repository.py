from typing import Optional, List
from injector import inject

from shop_food.contracts.abstract_model import AbstractModel
from shop_food.contracts.interface_db import InterfaceDB
from shop_food.infra.database.mongo.parse import Transform


class AbstractRepository:
    model = AbstractModel
    collection: str = ''
    transform: Transform

    @inject
    def __init__(self, db: InterfaceDB, transform: Transform):
        self.db = db
        self.transform = transform

    def all(self):
        items = []
        for item in self.db.find(self.collection):
            items.append(self.model(** self.relations(item)))

        return items

    def find_by_id(self, id_model: str) -> Optional[AbstractModel]:
        result = self.db.find_one(self.collection, id_model)

        if not result:
            return None

        return self.model(**self.relations(result))

    def add(self, model: AbstractModel) -> AbstractModel:
        item_dict = self.transform.prepare_obj(model.dict())
        self.validation_relations(item_dict)
        result = self.db.insert_one(self.collection, item_dict)

        return self.find_by_id(result)

    def update(
            self,
            id_model: str,
            prod: AbstractModel
    ) -> Optional[AbstractModel]:
        actual = self.find_by_id(id_model)
        if not actual:
            return None

        self.validation_relations(prod.dict())
        prod_dict = self.transform.merge(
            self.transform.prepare_obj(actual.dict()),
            self.transform.prepare_obj(prod.dict())
        )
        self.db.update_one(self.collection, id_model, prod_dict)

        return self.find_by_id(id_model)

    def delete(self, id_model: str) -> bool:
        return self.db.delete_one(self.collection, id_model)

    def find(self, query: dict) -> List[AbstractModel]:
        result = self.db.find(self.collection, query)
        items = []
        for item in result:
            items.append(self.model(** self.relations(item)))

        return items

    def find_one(self, query: dict) -> AbstractModel | None:
        result = self.db.find(self.collection, query)
        if len(result) == 0:
            return None

        return self.model(**self.relations(result[0]))

    def relations(self, model: dict) -> dict:
        return self.transform.prepare_model(model)

    def validation_relations(self, model) -> None:
        ...
