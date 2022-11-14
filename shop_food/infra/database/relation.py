from pydantic import BaseModel


class Relation(BaseModel):
    field: str
    model: str
    model_id: str = 'id'
    repository: type



