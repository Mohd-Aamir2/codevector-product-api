from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    category = Column(String, nullable=False)

    price = Column(Float, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )