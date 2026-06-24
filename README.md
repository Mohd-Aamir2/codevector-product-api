# Product Management API

A FastAPI-based Product Management API built for handling large product datasets with CRUD operations, search, validation, filtering, and cursor-based pagination.

## Features

* Create Product
* Get All Products
* Get Product by ID
* Update Product
* Delete Product
* Search Products by Name
* Category Filtering
* Cursor-Based Pagination
* Pydantic Validation
* SQLAlchemy ORM
* SQLite Database
* FastAPI Dependency Injection
* HTTP Exception Handling
* CORS Enabled for Frontend Integration
* Bulk Product Seeding (200,000 Products)

---

## Tech Stack

* FastAPI
* SQLAlchemy
* Pydantic
* SQLite
* Uvicorn
* Python 3.x

---

## Project Structure

```text
project/
│
├── routers/
│   └── products.py
│
├── database.py
├── models.py
├── schemas.py
├── main.py
├── seed_products.py
├── requirements.txt
└── README.md
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn main:app --reload
```

Application will be available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Database Seeding

Generate and insert 200,000 sample products:

```bash
python seed_products.py
```

---

## API Endpoints

### Get Products

```http
GET /products
```

Query Parameters:

| Parameter | Type   | Description           |
| --------- | ------ | --------------------- |
| limit     | int    | Number of records     |
| cursor    | int    | Cursor for pagination |
| category  | string | Filter by category    |

Example:

```http
GET /products?limit=20
```

```http
GET /products?limit=20&cursor=20
```

```http
GET /products?category=Electronics&limit=20
```

---

### Search Products

```http
GET /products/search?name=phone
```

---

### Get Product By ID

```http
GET /products/{product_id}
```

---

### Create Product

```http
POST /products
```

Request Body:

```json
{
  "name": "Monitor",
  "category": "Electronics",
  "price": 15000
}
```

---

### Update Product

```http
PUT /products/{product_id}
```

---

### Delete Product

```http
DELETE /products/{product_id}
```

---

### Count Products

```http
GET /count
```

---

## Pagination Strategy

This project uses Cursor-Based Pagination to efficiently handle large datasets and avoid issues associated with offset pagination.

Benefits:

* Faster queries on large datasets
* Better scalability
* Reduced risk of duplicate records
* Improved consistency while browsing data

---

## Validation

Pydantic validation is used to validate incoming requests.

Example:

```python
name: str = Field(min_length=2, max_length=100)
category: str = Field(min_length=2, max_length=50)
price: float
```

---

## Author

Mohd Aamir
