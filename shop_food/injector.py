import os

from flask import Flask
from flask_injector import FlaskInjector, request
from injector import Injector

from shop_food.dev_config import DevConfig
from shop_food.contracts.interface_db import InterfaceDB
from shop_food.infra.database.mongo.db import DB
from shop_food.infra.database.mongo.parse import Transform


def configure(binder):
    config_db = DevConfig().DATABASE.get('mongodb')
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


def boot_app(app: Flask) -> FlaskInjector:
    return FlaskInjector(app=app, modules=[configure])


def boot_injector() -> Injector:
    return Injector(modules=[configure])
