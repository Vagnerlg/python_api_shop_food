from shop_food.infra.database.db import DB
from shop_food.product.model import Product
from bson.objectid import ObjectId
from datetime import datetime
from typing import List, Optional, Any


class Repository(DB):
    collection: str = 'products'

    def all(self) -> List[Product]:
        products = []
        for product in self.get_collection().find():
            product['id'] = str(product['_id'])
            products.append(Product(**product))

        return products

    def find_by_id(self, id_prod: str) -> Optional[Product]:
        result = self.get_collection().find_one({
            '_id': ObjectId(id_prod)
        })

        if None == result:
            return None
        result['id'] = str(result['_id'])

        return Product(**result)

    def add(self, prod: Product) -> Product:
        self._set_date(prod)
        result = self.get_collection().insert_one(prod.dict())
        prod.id = str(result.inserted_id)

        return prod

    def update(self, id_prod: str, prod: Product) -> Product:
        prod_dict = self._merge(self.find_by_id(id_prod), prod)
        self.get_collection().update_one({
            '_id': ObjectId(id_prod)
        }, {
            '$set': prod_dict
        })

        return self.find_by_id(id_prod)

    def delete(self, id_prod: str) -> bool:
        result = self.get_collection().delete_one({
            '_id': ObjectId(id_prod)
        })
        if 0 < result.deleted_count.bit_count():
            return True
        return False

    def _set_date(self, prod: Product) -> None:
        if None == prod.created_at:
            prod.created_at = datetime.now()
        prod.updated_at = datetime.now()

    def _merge(self, current: Product, actual: Product) -> dict[str, Any]:
        new_prod = actual.dict()
        del new_prod['created_at']
        del new_prod['updated_at']
        self._set_date(current)
        prod_dict = current.dict() | new_prod
        del prod_dict['id']

        return prod_dict
