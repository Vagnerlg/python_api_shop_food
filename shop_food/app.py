from flask import Flask
from flask_injector import FlaskInjector

from shop_food.dev_config import DevConfig
from shop_food.injector import boot_app
from shop_food.order.route import map_route as order_map_route
from shop_food.product.route import map_route as product_map_route


def load_app(env: str) -> FlaskInjector:

    # init app flask
    app = Flask(__name__)

    # load configFile and env configuration
    if 'unit_testing' == env:
        app.config.update({
            "TESTING": True,
        })

    app.config.from_object(DevConfig)

    # init dependency inject
    f_injector = boot_app(app)

    # init Routes
    product_map_route(f_injector)
    order_map_route(f_injector)

    return f_injector


f_injector = load_app('develop')
app = f_injector.app
