from app.logger import logger

def process_payment(order):
    logger.info(
        "Received Order=%s Customer=%s Amount=%s",
        order["order_id"],
        order["customer"],
        order["amount"]
    )

    logger.info("Processing payment...")

    if order.get("simulate_failure", False):
        logger.error(
            "Order=%s Payment Gateway Unavailable",
            order["order_id"]
        )                                                                  
        raise Exception("Payment Gateway Unavailable")


    logger.info(
    "Order=%s Payment Successful",
    order["order_id"]
    )