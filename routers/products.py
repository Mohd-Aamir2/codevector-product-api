from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Product
from schemas import ProductResponse, ProductCreate


router = APIRouter()


@router.get("/products")
def get_products(
    limit: int = 20,
    category: str | None = None,
    cursor: int | None = None,
    db: Session = Depends(get_db)
):

    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)

    if cursor:
        query = query.filter(Product.id > cursor)

    products = (
        query
        .order_by(Product.updated_at.desc(), Product.id.desc())
        .limit(limit)
        .all()
    )

    next_cursor = None

    if products:
        next_cursor = products[-1].id

    return {
        "data": products,
        "next_cursor": next_cursor
    }

@router.post(
    "/products",
    response_model=ProductResponse,
    status_code=201
)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    

    new_product = Product(
    name=product.name,
    category=product.category,
    price=product.price
)

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return new_product

@router.get(
    "/products/search",
    response_model=list[ProductResponse]
)
def search_products(
    name: str,
    db: Session = Depends(get_db)
):
    products = (
        db.query(Product)
        .filter(Product.name.ilike(f"%{name}%"))
        .all()
    )

    return products   


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    db_product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not db_product:
        raise HTTPException(
        status_code=404,
        detail="Product not found"
        )

    db_product.name = product.name
    db_product.category = product.category
    db_product.price = product.price

    db.commit()
    db.refresh(db_product)

    return db_product

@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    db_product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not db_product:
        raise HTTPException(
        status_code=404,
        detail="Product not found"
        )

    db.delete(db_product)

    db.commit()

    return {"message": "Product deleted successfully"}


@router.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
): 
    
    db_product = (
    db.query(Product)
    .filter(Product.id == product_id)
    .first()
)
    if not db_product:
      raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

    return db_product

@router.get("/count")
def count_products(db: Session = Depends(get_db)):
    return {
        "count": db.query(Product).count()
    }