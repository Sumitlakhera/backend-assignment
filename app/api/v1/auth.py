import re
from tokenize import Token

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.auth import (
    UserRegisterRequest,
    UserResponse,
    LoginRequest,
    TokenResponse
)
from app.services.auth_service import register_user, authenticate_user

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
    

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    try:
        user = authenticate_user(
            db=db,
            email=login_data.email,
            password=login_data.password
        )

        return user
    
    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
