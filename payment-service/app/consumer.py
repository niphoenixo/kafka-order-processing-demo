import json

from confluent_kafka import Consumer
from dotenv import load_dotenv
from pathlib import Path
import os
import random
from app.kafka.producer import publish_retry_order
from app.logger import logger

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

print("Kafka:", os.getenv("KAFKA_BOOTSTRAP_SERVERS"))
print("Topic:", os.getenv("ORDER_TOPIC"))
print("Group:", os.getenv("GROUP_ID"))


from app.kafka.consumer_factory import create_consumer

consumer = create_consumer(os.getenv("GROUP_ID"))

consumer.subscribe([os.getenv("ORDER_TOPIC")])


print("Payment Service Started...")
print("Waiting for orders...\n")



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
        #print("=" * 50)

while True:

    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print(msg.error())
        continue

    order = json.loads(msg.value().decode("utf-8"))

    try:
        process_payment(order)

    except Exception as e:
        print(f"\n❌ Payment Failed : {order['order_id']}")
        print(str(e))
        logger.error(
            "Order=%s Payment Failed",
            order["order_id"]
        )
        publish_retry_order(order)