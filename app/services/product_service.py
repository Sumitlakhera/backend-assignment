from sqlalchemy.orm import Session

from app.repositories.product_repository import create_product


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