from itertools import product
import re

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


def get_all_products(
        db: Session
):
    return db.query(Product).all()



def get_product_by_id(
    db: Session,
    product_id: int
):
    return db.query(Product).filter(Product.id == product_id).first()



def update_product(
        db: Session,
        product: Product,
        name: str,
        description: str,
        price: float
):
    product.name = name
    product.description = description
    product.price = price

    db.commit()
    db.refresh(product) 

    return product

def delete_product(
        db: Session,
        product: Product
):
    db.delete(product)
    db.commit()