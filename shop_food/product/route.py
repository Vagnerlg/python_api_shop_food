from flask import Flask
from shop_food.infra.http.base_controller import BaseController
from .controller.product_controller import ProductController
from .repository.category_repository import CategoryRepository
from .repository.product_repository import ProductRepository


def map_route(app: Flask) -> None:

    def route_crud(model_name: str, controller: BaseController) -> None:
        app.add_url_rule('/' + model_name, endpoint=model_name + '.items', view_func=controller.items)
        app.add_url_rule('/' + model_name, endpoint=model_name + '.add', view_func=controller.add, methods=['POST'])
        app.add_url_rule('/' + model_name + '/<id_model>', endpoint=model_name + '.item', view_func=controller.item)
        app.add_url_rule(
            '/' + model_name + '/<id_model>',
            endpoint=model_name + '.update',
            view_func=controller.update,
            methods=['POST', 'PUT']
        )
        app.add_url_rule(
            '/' + model_name + '/<id_model>',
            endpoint=model_name + '.delete',
            view_func=controller.delete,
            methods=['DELETE']
        )

    product_controller = BaseController(
        repository=ProductRepository()
    )

    category_controller = BaseController(
        repository=CategoryRepository()
    )

    route_crud('product', product_controller)
    route_crud('category', category_controller)

    app.add_url_rule(
        '/product/category/<id_cat>',
        endpoint='category_all_product.update',
        view_func=ProductController(
            repository=ProductRepository()
        ).all_products
    )
