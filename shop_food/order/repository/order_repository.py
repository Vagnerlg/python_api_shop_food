from shop_food.infra.database.abstract_repository import AbstractRepository
from shop_food.infra.database.util.parse import prepare_obj
from shop_food.infra.http.request.add_order_item import AddOrderItem
from shop_food.order.model.order import Order


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

        payload = prepare_obj(order.dict())
        result = self.get_db().insert_one(payload)

        # busca por pedido com status CREATED, se não encontra cria um
        # adiciona o produto e sua quantidade
        # retorna o Pedido
        return self.find_by_id(str(result.inserted_id))
