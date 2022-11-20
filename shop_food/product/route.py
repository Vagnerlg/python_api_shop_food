from flask_injector import FlaskInjector

from shop_food.infra.http.base_controller import BaseController
from .controller.product_controller import ProductController
from .repository.category_repository import CategoryRepository
from .repository.product_repository import ProductRepository
from ..infra.http.route_crud import route_crud


def map_route(flask_injector: FlaskInjector) -> None:
    app = flask_injector.app
    injector = flask_injector.injector

    product_controller = BaseController(
        repository=injector.get(ProductRepository)
    )

    category_controller = BaseController(
        repository=injector.get(CategoryRepository)
    )

    route_crud(app, 'category', category_controller)
    route_crud(app, 'product', product_controller)

    app.add_url_rule(
        '/product/category/<id_cat>',
        endpoint='category_all_product.update',
        view_func=ProductController(
            repository=injector.get(ProductRepository)
        ).all_products
    )
