from fastapi import APIRouter

from app.models.order import Order

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("")
def create_order(order: Order):
    return {
        "message": "Order received successfully",
        "order": order
    }