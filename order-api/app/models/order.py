from pydantic import BaseModel, Field
from typing import List


class OrderItem(BaseModel):
    product: str
    quantity: int = Field(..., gt=0)


class Order(BaseModel):
    order_id: str
    customer: str
    amount: float = Field(..., gt=0)
    items: List[OrderItem]