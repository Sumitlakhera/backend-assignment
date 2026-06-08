from re import S

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime

from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer, 
        primary_key=True, 
        index=True
    )
    
    name = Column(
        String(100), 
        nullable=False
    )

    email = Column(
        String(255), 
        unique=True, 
        index=True, 
        nullable=False
    )

    hashed_password = Column(
        String(255), 
        nullable=False
    )

    role = Column(
        String(50), 
        default= "user"
    )
    created_at = Column(
        DateTime, 
        default=datetime.utcnow()
    )

    products = relationship(
        "Product", 
        back_populates="owner"
    )


class Product(Base):
    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(255),
        nullable=True
    )

    price = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    owner = relationship(
        "User",
        back_populates="products"
    )