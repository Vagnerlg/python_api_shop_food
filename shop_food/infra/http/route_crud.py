from flask import Flask

from shop_food.infra.http.base_controller import BaseController


def route_crud(
        app: Flask,
        model_name: str,
        controller: BaseController
) -> None:

    app.add_url_rule(
        '/' + model_name,
        endpoint=model_name + '.items',
        view_func=controller.items
    )

    app.add_url_rule(
        '/' + model_name,
        endpoint=model_name + '.add',
        view_func=controller.add,
        methods=['POST']
    )

    app.add_url_rule(
        '/' + model_name + '/<id_model>',
        endpoint=model_name + '.item',
        view_func=controller.item
    )

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
