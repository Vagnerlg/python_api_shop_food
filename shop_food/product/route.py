from flask import Flask
from .controller import products, product, add_product, update_product, delete_product


def map_route(app: Flask) -> None:
    app.add_url_rule('/product', view_func=products)
    app.add_url_rule('/product/<id_prod>', view_func=product)
    app.add_url_rule('/product', view_func=add_product, methods=['POST'])
    app.add_url_rule('/product/<id_prod>', view_func=update_product, methods=['POST', 'PUT'])
    app.add_url_rule('/product/<id_prod>', view_func=delete_product, methods=['DELETE'])
