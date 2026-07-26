from fastapi import APIRouter

from app.models.order import Order
from app.services.order_service import OrderService

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("")
def create_order(order: Order):
    return OrderService.create_order(order)