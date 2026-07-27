import json

from confluent_kafka import Consumer
from dotenv import load_dotenv
import os

from pathlib import Path

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

print("Kafka:", os.getenv("KAFKA_BOOTSTRAP_SERVERS"))
print("Topic:", os.getenv("ORDER_TOPIC"))
print("Group:", os.getenv("GROUP_ID"))


consumer = Consumer({
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    "group.id": os.getenv("GROUP_ID"),
    "auto.offset.reset": "earliest"
})

consumer.subscribe([os.getenv("ORDER_TOPIC")])


print("Payment Service Started...")
print("Waiting for orders...\n")


while True:

    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print(msg.error())
        continue

    try:
        order = json.loads(msg.value().decode("utf-8"))
    except json.JSONDecodeError:
        print(f"Skipping invalid message: {msg.value().decode('utf-8')}")
        continue

    print("=" * 50)
    print(f"Received Order : {order['order_id']}")
    print(f"Customer       : {order['customer']}")
    print(f"Amount         : {order['amount']}")
    print("Processing Payment...")
    print("✅ Payment Successful")
    print("=" * 50)