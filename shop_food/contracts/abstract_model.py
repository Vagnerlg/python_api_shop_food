from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime


class AbstractModel(BaseModel):
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @validator('created_at', 'updated_at', always=True)
    def validate_date(cls, v) -> datetime:
        return v or datetime.now()
