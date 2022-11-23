from flask import Flask
from flask_injector import FlaskInjector, request

from shop_food.infra.database.db import DB
from shop_food.infra.database.util.parse import Transform


def boot_injector(app: Flask):

    def configure(binder):
        config_db = app.config['DATABASE']['mongodb']
        db = DB(config_db)
        # config_collection = app.config['REPOSITORIES']
        transform = Transform()

        binder.bind(
            DB,
            to=db,
            scope=request,
        )

        binder.bind(
            Transform,
            to=transform,
            scope=request,
        )

    return FlaskInjector(app=app, modules=[configure])
