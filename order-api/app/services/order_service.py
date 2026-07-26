from app.kafka.producer import publish_order


class OrderService:

    @staticmethod
    def create_order(order):
        publish_order(order.model_dump())

        return {
            "message": "Order published successfully",
            "order": order
        }