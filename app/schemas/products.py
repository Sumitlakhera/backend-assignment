from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProductCreateRequest(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )

    description: str = Field(
        min_length=5,
        max_length=500
    )

    price: float = Field(
        gt=0
    )


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

class ProductUpdateRequest(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )

    description: str = Field(
        min_length=5,
        max_length=500
    )

    price: float = Field(
        gt=0
    )