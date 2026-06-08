from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductCreateRequest(BaseModel):
    name: str
    description: str
    price: float


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )