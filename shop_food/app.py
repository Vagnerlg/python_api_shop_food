import os

from dotenv import load_dotenv
from flask import Flask

from shop_food.config import DevConfig
from shop_food.injector import boot_injector
from shop_food.order.route import map_route as order_map_route
from shop_food.product.route import map_route as product_map_route

# load file .env
load_dotenv()

# init app flask
app = Flask(__name__)

# load configFile and env configuration
if 'develop' == os.getenv('ENV'):
    app.config.from_object(DevConfig)

# init dependency inject
flask_injector = boot_injector(app)

# init Routes
product_map_route(flask_injector)
order_map_route(flask_injector)
