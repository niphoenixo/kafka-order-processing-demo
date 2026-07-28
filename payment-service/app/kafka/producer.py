import json
import os

from confluent_kafka import Producer
from dotenv import load_dotenv

load_dotenv()

producer = Producer({
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS")
})

def publish_dlq_order(order: dict):

    producer.produce(
        topic=os.getenv("PAYMENT_DLQ_TOPIC"),
        key=order["order_id"],
        value=json.dumps(order)
    )

    producer.flush()

    print(f"💀 Sent {order['order_id']} to Dead Letter Queue")

def publish_retry_order(order: dict):

    order["retry_count"] = order.get("retry_count", 0) + 1

    producer.produce(
        topic=os.getenv("PAYMENT_RETRY_TOPIC"),
        key=order["order_id"],
        value=json.dumps(order)
    )

    producer.flush()

    print(
        f"🔁 Sent {order['order_id']} "
        f"to payment-retry "
        f"(Attempt {order['retry_count']})"
    )