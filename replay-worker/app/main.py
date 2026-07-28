import json

from app.consumer import consumer
from app.producer import replay_order

print("=" * 60)
print("Replay Worker Started")
print("Listening on payment-dlq...")
print("=" * 60)

while True:

    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print(msg.error())
        continue

    order = json.loads(msg.value().decode())

    print("\nReplaying Order:", order["order_id"])

    replay_order(order)