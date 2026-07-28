import json
import os

from confluent_kafka import Producer
from dotenv import load_dotenv

load_dotenv()

producer = Producer({
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS")
})


def replay_order(order: dict):

    # Payment gateway is now healthy
    order["simulate_failure"] = False

    # Fresh retry cycle
    order["retry_count"] = 0

    producer.produce(
        topic=os.getenv("ORDER_TOPIC"),
        key=order["order_id"],
        value=json.dumps(order)
    )

    producer.flush()

    print(f"♻️ Replayed {order['order_id']} back to orders topic")