from flask import request
from pydantic import ValidationError

from shop_food.infra.http.base_controller import BaseController
from shop_food.infra.http.request.add_order_item import AddOrderItem
from shop_food.infra.http.response import response_success, response_errors
from shop_food.order.repository.order_repository import OrderRepository


class OrderController(BaseController):

    repository = OrderRepository

    def add_item(self):
        try:
            item = AddOrderItem(**request.get_json())
            self.repository.add_item(item)
            return response_success(item.dict())
        except ValidationError as e:
            return response_errors(e.errors())

