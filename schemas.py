from pydantic import BaseModel, Field

class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    price: float

    model_config = {
        "from_attributes": True
    }

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    
    category: str = Field(min_length=2, max_length=50)
    price: float 