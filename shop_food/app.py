from flask import Flask, request
from flask_injector import FlaskInjector

from shop_food.config import Config
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

    app.config.from_object(Config)

    def test():
        return {
            'headers': dict(request.headers),
            'body': request.get_json()
        }

    app.add_url_rule(
        '/wai/webhooks',
        endpoint='wai.tests',
        view_func=test,
        methods=['POST', 'GET']
    )

    # init dependency inject
    f_injector = boot_app(app)

    # init Routes
    product_map_route(f_injector)
    order_map_route(f_injector)

    return f_injector


f_injector = load_app('develop')
app = f_injector.app
