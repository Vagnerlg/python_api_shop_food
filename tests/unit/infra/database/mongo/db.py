from shop_food.contracts.interface_db import InterfaceDB


class DB(InterfaceDB):
    data: list[dict]
    index: int = 0

    def expected(self, data: list[dict]) -> None:
        self.data = data

    def __get_expected(self) -> dict:
        result = self.data[self.index]
        self.index = self.index + 1

        return result

    def find(self, collection: str, query: dict = {}) -> list[dict]:
        result = self.__get_expected()

        assert result.get('params').get('query') == query

        return result.get('result')

    def find_one(self, collection: str, id_model: str) -> dict | None:
        result = self.__get_expected()

        assert result.get('params').get('id_model') == id_model

        return result.get('result')

    def insert_one(self, collection: str, data: dict) -> str | None:
        result = self.__get_expected()

        assert data.get('created_at') is not None
        assert data.get('updated_at') is not None
        del data['created_at']
        del data['updated_at']

        if result.get('result').get('inserted_id') is not None:
            return str(result.get('result').get('inserted_id'))

        return None

    def update_one(self, collection: str, id: str, data: dict) -> None:
        result = self.__get_expected()

        assert result.get('params').get('id') == id
        assert data.get('created_at') is not None
        assert data.get('updated_at') is not None
        del data['created_at']
        del data['updated_at']

        return None

    def delete_one(self, collection: str, id: str) -> bool:
        result = self.__get_expected()
        assert result.get('params').get('id') == id

        return True
