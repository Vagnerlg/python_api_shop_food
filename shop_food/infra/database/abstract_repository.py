from typing import Optional, List
from bson import ObjectId
from shop_food.infra.database.base_model import BaseModel
from shop_food.infra.database.util_model import UtilModel


class AbstractRepository(UtilModel):
    model = BaseModel

    def all(self) -> List[BaseModel]:
        items = []
        for item in self.get_collection().find():
            item['id'] = str(item['_id'])
            item = self.embed(item)
            items.append(self.model(**item))

        return items

    def find_by_id(self, id_model: str) -> Optional[BaseModel]:
        result = self.get_collection().find_one({
            '_id': ObjectId(id_model)
        })

        if None == result:
            return None

        result['id'] = str(result['_id'])
        result = self.embed(result)
        return self.model(**result)

    def add(self, model: BaseModel) -> BaseModel:
        self.set_date(model)
        prod_dict = self.relations_obj(model)
        result = self.get_collection().insert_one(prod_dict)
        model.id = str(result.inserted_id)

        return model

    def update(self, id_model: str, prod: BaseModel) -> BaseModel:
        prod_dict = self.merge(self.find_by_id(id_model), prod)
        self.get_collection().update_one({
            '_id': ObjectId(id_model)
        }, {
            '$set': prod_dict
        })

        return self.find_by_id(id_model)

    def delete(self, id_model: str) -> bool:
        result = self.get_collection().delete_one({
            '_id': ObjectId(id_model)
        })
        if 0 < result.deleted_count.bit_count():
            return True
        return False

    def find(self, query: dict) -> List[BaseModel]:
        result = self.get_collection().find(query)
        items = []
        print(result)
        for item in result:
            item['id'] = str(item['_id'])
            item = self.embed(item)
            items.append(self.model(**item))

        return items
