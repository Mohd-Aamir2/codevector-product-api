from database import SessionLocal
from models import Product
from datetime import datetime, UTC
import random




categories = [
    "Electronics",
    "Books",
    "Fashion",
    "Sports",
    "Home"
]

session = SessionLocal()

products = []

for i in range(1, 200001):

    product = Product(
        name=f"Product {i}",
        category=random.choice(categories),
        price=round(random.uniform(100, 5000), 2),
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC)
    )

    products.append(product)

    if i % 10000 == 0:
        print(f"Generated {i} products...")

batch_size = 10000

for start in range(1, 200001, batch_size):

    products = []

    for i in range(start, start + batch_size):

        product = Product(
            name=f"Product {i}",
            category=random.choice(categories),
            price=round(random.uniform(100, 5000), 2),
            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC)
        )

        products.append(product)

    session.bulk_save_objects(products)
    session.commit()

    print(f"Inserted {min(start + batch_size - 1, 200000)} products")

