import os

from shop_food.injector import boot_injector


def boot():
    os.environ["ENV"] = 'unit_testing'
    return boot_injector()
