from flask_injector import FlaskInjector

from shop_food.order.controller.order_controller import OrderController
from shop_food.order.repository.order_repository import OrderRepository


def map_route(flask_injector: FlaskInjector) -> None:
    app = flask_injector.app
    injector = flask_injector.injector

    order_controller = OrderController(
        repository=injector.get(OrderRepository)
    )

    app.add_url_rule('/order', endpoint='order.items', view_func=order_controller.items)

    app.add_url_rule(
        '/order/add_item',
        endpoint='order.add_item',
        view_func=order_controller.add_item,
        methods=['POST']
    )
