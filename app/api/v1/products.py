from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import User

from app.schemas.products import (
    ProductCreateRequest,
    ProductResponse
)

from app.services.product_service import create_new_product

from app.api.dependencies.auth import get_current_user


router = APIRouter()


@router.post(
    "",
    response_model=ProductResponse,
    status_code=201
)
def create_product(
    request: ProductCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = create_new_product(
        db=db,
        name=request.name,
        description=request.description,
        price=request.price,
        owner_id=current_user.id
    )

    return product