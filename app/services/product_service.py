from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories.product_repository import( 
    create_product, 
    get_all_products, 
    get_product_by_id,
    update_product,
    delete_product

)


def create_new_product(
    db: Session,
    name: str,
    description: str,
    price: float,
    owner_id: int
):
    product = create_product(
        db=db,
        name=name,
        description=description,
        price=price,
        owner_id=owner_id
    )

    return product


def list_products(
    db: Session
):
    return get_all_products(db)

def get_product(
    db: Session,
    product_id: int
):
    product = get_product_by_id(
        db=db,
        product_id=product_id
    )

    if not product:
        raise ValueError("Product not found")
    
    return product


def verify_product_access(
    product,
    current_user
):
    if (
        product.owner_id != current_user.id
        and current_user.role != "admin"
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to modify this product"
        )


def update_existing_product(
    db: Session,
    product_id: int,
    name: str,
    description: str,
    price: float,
    current_user
):
    product = get_product_by_id(
        db=db,
        product_id=product_id
    )


    if product is None:
        raise ValueError("Product not found")
    
    verify_product_access(
        product=product,
        current_user=current_user
    )

    return update_product(
        db=db,
        product=product,
        name=name,
        description=description,
        price=price
    )



def delete_existing_product(
        db: Session,
        product_id: int,
        current_user
):
    product = get_product_by_id(
        db=db,
        product_id=product_id
    )
    if product is None:
        raise ValueError("Product not found")
    
    verify_product_access(
        product=product,
        current_user=current_user
    )

    return delete_product(
        db=db,
        product=product
    )