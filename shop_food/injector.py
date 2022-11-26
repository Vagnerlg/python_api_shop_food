from flask import Flask
from flask_injector import FlaskInjector, request

from shop_food.contracts.interface_db import InterfaceDB
from shop_food.infra.database.mongo.db import DB
from shop_food.infra.database.mongo.parse import Transform


def boot_injector(app: Flask):

    def configure(binder):
        config_db = app.config['DATABASE']['mongodb']
        db = DB(config_db)
        transform = Transform()

        binder.bind(
            InterfaceDB,
            to=db,
            scope=request,
        )

        binder.bind(
            Transform,
            to=transform,
            scope=request,
        )

    return FlaskInjector(app=app, modules=[configure])
