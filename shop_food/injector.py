from flask import Flask
from flask_injector import FlaskInjector, request

from shop_food.infra.database.db import DB


def boot_injector(app: Flask):

    def configure(binder):
        config_db = app.config['DATABASE']['mongodb']
        db = DB(config_db)

        binder.bind(
            DB,
            to=db,
            scope=request,
        )

    return FlaskInjector(app=app, modules=[configure])
