from shop_food.infra.database.abstract_repository import AbstractRepository
from shop_food.infra.http.form_request.add_order_item import AddOrderItem
from shop_food.order.model.order import Order
from shop_food.product.repository.product_repository import ProductRepository


class OrderRepository(AbstractRepository):
    collection: str = 'orders'
    model = Order

    def add_item(self, form_item: AddOrderItem):
        add_dict = form_item.dict()

        order = Order(**{
            'user': {
                add_dict['user']['type']: add_dict['user']['value']
            },
            'items': [
                {
                    'product': add_dict['product'],
                    'quantity': add_dict['quantity']
                }
            ],
            'status': 'created'
        })

        payload = self.transform.prepare_obj(order.dict())
        result = self.get_db().insert_one(payload)

        # busca por pedido com status CREATED, se não encontra cria um
        # adiciona o produto e sua quantidade
        # retorna o Pedido
        return self.find_by_id(str(result.inserted_id))

    def relations(self, model: dict) -> dict:
        items = model.get('items')

        if not items:
            return self.transform.prepare_model(model)

        items_obj = []
        for item in items:
            product = ProductRepository(self.db, self.transform).find_by_id(item.get('product_id'))
            if not product:
                item['product'] = {
                    'title': 'not found',
                    'short_description': 'not found',
                    'description': 'not found',
                    'category': {
                        'name': 'not found'
                    },
                    'price': 0
                }
            else:
                item['product'] = product
            items_obj.append(self.transform.prepare_model(item))
        model['items'] = items

        return self.transform.prepare_model(model)
