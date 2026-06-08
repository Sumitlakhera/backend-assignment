from sqlalchemy.orm import Session
from app.db.models import Product

def create_product(
    db: Session,
    name: str,
    description: str,
    price: float,
    owner_id: int
):
    product = Product(
        name=name,
        description=description,
        price=price,
        owner_id=owner_id
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product