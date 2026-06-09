from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import User

from app.schemas.products import (
    ProductCreateRequest,
    ProductResponse,
    ProductUpdateRequest
)

from app.services.product_service import (
    create_new_product,
    list_products, 
    get_product,
    update_existing_product,
    delete_existing_product
)

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

@router.get(
    "",
    response_model=list[ProductResponse]
)
def get_products(
    db: Session = Depends(get_db)
):
    return list_products(db)

@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):
    try: 
        return get_product(
            db=db,
            product_id=product_id
        )
    except ValueError as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=str(e))
    

@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product_by_id(
    product_id: int,
    request: ProductUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return update_existing_product(
            db=db,
            product_id=product_id,
            name=request.name,
            description=request.description,
            price=request.price,
            current_user=current_user
        )
    except ValueError as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=str(e)
)
    

@router.delete(
    "/{product_id}",
    status_code=204
)
def delete_product_by_id(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return delete_existing_product(
            db=db,
            product_id=product_id,
            current_user=current_user
        )
    except ValueError as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=str(e))