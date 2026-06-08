import re

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.auth import (
    UserRegisterRequest,
    UserResponse
)
from app.services.auth_service import register_user

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    request: UserRegisterRequest,
    db: Session = Depends(get_db)
):
    try:
        user= register_user(
            db=db,
            name=request.name,
            email=request.email,
            password=request.password
        )

        return user
    
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )