import os

from shop_food.injector import boot_injector


def boot(env: str):
    os.environ["ENV"] = env
    return boot_injector()
