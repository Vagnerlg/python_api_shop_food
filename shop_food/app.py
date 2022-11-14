from dotenv import load_dotenv
from flask import Flask

from .order.route import map_route_order
from .product.route import map_route

load_dotenv()
app = Flask(__name__)
map_route(app)
map_route_order(app)
