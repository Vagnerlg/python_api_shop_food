from flask_injector import FlaskInjector

from shop_food.infra.database.db import DB
from shop_food.order.controller.order_controller import OrderController
from shop_food.order.repository.order_repository import OrderRepository


def map_route(flask_injector: FlaskInjector) -> None:
    app = flask_injector.app
    injector = flask_injector.injector

    order_controller = OrderController(
        repository=OrderRepository(injector.get(DB))
    )

    app.add_url_rule(
        '/order/add_item',
        endpoint='order.add_item',
        view_func=order_controller.add_item,
        methods=['POST']
    )
