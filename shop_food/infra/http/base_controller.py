from shop_food.infra.database.abstract_repository import AbstractRepository
from shop_food.product.model.product import Product
from shop_food.product.repository.product_repository import ProductRepository
from flask import request
from pydantic import ValidationError, BaseModel as BaseModelPydantic
from shop_food.infra.http.response import response_errors, response_success

repository = ProductRepository
model = Product


class BaseController(BaseModelPydantic):
    repository: AbstractRepository

    def items(self):
        result = self.repository.all()
        return response_success([item.dict() for item in result])

    def item(self, id_model: str):
        result = self.repository.find_by_id(id_model)
        if None == result:
            return response_errors({
                    'product': 'not_found'
                })

        return response_success(result.dict())

    def add(self):
        try:
            item_model = model(** request.get_json())
            result = self.repository.add(item_model)
            return response_success(result.dict())
        except ValidationError as e:
            return response_errors(e.errors())

    def update(self, id_model: str):
        try:
            item_model = model(** request.get_json())
            result = self.repository.update(id_model, item_model)
            return response_success(result.dict())
        except ValidationError as e:
            return response_errors(e.errors())

    def delete(self, id_model: str):
        try:
            result = self.repository.delete(id_model)
            if result:
                return response_success({
                    'delete': True
                })
            return response_errors({
                    'delete': False
                })
        except ValidationError as e:
            return response_errors(e.errors())