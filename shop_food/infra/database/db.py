from pymongo import MongoClient
from pymongo.database import Database


class DB:
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

    def get_collection(self, collection: str):
        return self.client_database[collection]
