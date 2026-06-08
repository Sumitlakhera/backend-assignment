from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.auth import (
    UserRegisterRequest,
    UserResponse,
    LoginRequest,
    TokenResponse
)
from app.services.auth_service import register_user, authenticate_user
from app.api.dependencies.auth import get_current_user, require_admin
from app.db.models import User

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
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    try:
        user = authenticate_user(
            db=db,
            email=form_data.username,
            password=form_data.password
        )

        return user
    
    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )


@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user

@router.get("/admin-only")
def admin_only_route(
    current_user: User = Depends(require_admin)
):
    return {
        "message": "Welcome Admin",
        "user": current_user.email
    }