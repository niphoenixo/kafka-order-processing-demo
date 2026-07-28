import json

from confluent_kafka import Consumer
from dotenv import load_dotenv
from pathlib import Path
import os
import random
from app.kafka.producer import publish_retry_order

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
    print("=" * 50)
    print(f"Received Order : {order['order_id']}")
    print(f"Customer       : {order['customer']}")
    print(f"Amount         : {order['amount']}")
    print("Processing Payment...")

    if random.random() < 0.4:
        raise Exception("Payment Gateway Unavailable")

    print("✅ Payment Successful")
    print("=" * 50)

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

        publish_retry_order(order)