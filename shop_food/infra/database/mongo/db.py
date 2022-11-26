from bson import ObjectId
from pymongo import MongoClient
from pymongo.database import Database

from shop_food.contracts.interface_db import InterfaceDB


class DB(InterfaceDB):
    client_database: Database

    def __init__(self, db_config: dict):
        client = MongoClient(
            'mongodb://' +
            db_config['user'] + ':' +
            db_config['password'] + '@' +
            db_config['url'] + ':' +
            str(db_config['port']) + '/'
        )
        self.client_database = client[db_config['name']]

    def __get_collection(self, collection: str):
        return self.client_database[collection]

    def find(self, collection: str, query: dict = {}) -> list[dict]:
        return list(self.__get_collection(collection).find(query))

    def find_one(self, collection: str, id_model: str) -> dict | None:
        return self.__get_collection(collection).find_one({
            '_id': ObjectId(id_model)
        })

    def insert_one(self, collection: str, data: dict) -> str | None:
        result = self.__get_collection(collection).insert_one(data)

        if not result.inserted_id:
            return None

        return str(result.inserted_id)

    def update_one(self, collection: str, id: str, data: dict) -> None:
        self.__get_collection(collection).update_one({
            '_id': ObjectId(id)
        }, {
            '$set': data
        })

    def delete_one(self, collection: str, id: str) -> bool:
        result = self.__get_collection(collection).delete_one({
            '_id': ObjectId(id)
        })
        if 0 < result.deleted_count.bit_count():
            return True
        return False
