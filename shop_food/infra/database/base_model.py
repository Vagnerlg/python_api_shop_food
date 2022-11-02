from pydantic import BaseModel as PydanticBaseModel
from typing import Optional
from datetime import datetime


class BaseModel(PydanticBaseModel):
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
