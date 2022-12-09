from shop_food.infra.http.base_controller import BaseController
from shop_food.infra.http.response import response_success


class ProductController(BaseController):
    def all_products(self, id_cat):
        all_items = self.repository.all_products_by_category(id_cat)
        return response_success([prod.dict() for prod in all_items])
