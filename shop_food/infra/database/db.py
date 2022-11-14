import os

from pydantic import BaseModel
from pymongo import MongoClient


class DB(BaseModel):
    collection: str = ''

    def get_collection(self, collection: str = None):
        client = MongoClient(
            os.getenv('DB_DRIVE') + '://' +
            os.getenv('DB_USER') + ':' +
            os.getenv('DB_PASSWORD') + '@' +
            os.getenv('DB_URL') + ':' +
            os.getenv('DB_PORT') + '/'
        )

        if None == collection:
            return client[os.getenv('DB_NAME')][self.collection]

        return client[os.getenv('DB_NAME')][collection]