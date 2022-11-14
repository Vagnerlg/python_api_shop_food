from flask import Flask

from shop_food.order.controller.order_controller import OrderController
from shop_food.order.repository.order_repository import OrderRepository


def map_route_order(app: Flask) -> None:
    order_controller = OrderController(
        repository=OrderRepository()
    )
    app.add_url_rule('/order/add_item', endpoint='order.add_item', view_func=order_controller.add_item, methods=['POST'])
