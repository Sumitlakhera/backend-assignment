from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime

class UserRegisterRequest(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=128
    )


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    created_at: datetime

    model_config=ConfigDict(
        from_attributes=True
    )