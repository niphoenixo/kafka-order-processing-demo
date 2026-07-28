import json
import os
import time

from app.kafka.consumer_factory import create_consumer
from app.handlers.payment_handler import process_payment
from dotenv import load_dotenv
from app.kafka.producer import (
    publish_retry_order,
    publish_dlq_order
)

load_dotenv()

consumer = create_consumer("payment-retry-group")

consumer.subscribe([os.getenv("PAYMENT_RETRY_TOPIC")])

print("=" * 60)
print("Retry Consumer Started")
print("Listening on payment-retry topic...")
print("=" * 60)


while True:

    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print(msg.error())
        continue

    order = json.loads(msg.value().decode())

    print(f"\nRetry Attempt #{order.get('retry_count', 1)}")

    time.sleep(5)

    try:

        process_payment(order)

        print("✅ Retry Successful")

    except Exception:

        retry_count = order.get("retry_count", 1)

        max_retry = int(os.getenv("MAX_RETRY_COUNT"))

        if retry_count >= max_retry:

            publish_dlq_order(order)

            print(
                f"💀 Max retry reached ({retry_count}). "
                f"Moved to DLQ."
            )

        else:

            publish_retry_order(order)

            print(
                f"🔁 Retry Failed "
                f"(Attempt {retry_count})"
            )