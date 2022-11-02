from pydantic import BaseModel
from pymongo import MongoClient
import os

class DB(BaseModel):
    collection: str = ''

    def get_collection(self):
        client = MongoClient(
            os.getenv('DB_DRIVE') + '://' +
            os.getenv('DB_USER') + ':' +
            os.getenv('DB_PASSWORD') + '@' +
            os.getenv('DB_URL') + ':' +
            os.getenv('DB_PORT') + '/'
        )

        return client[os.getenv('DB_NAME')][self.collection]
