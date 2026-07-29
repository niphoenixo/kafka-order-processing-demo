from confluent_kafka import Consumer

consumer = Consumer({
    "bootstrap.servers": "localhost:29092",

    "group.id": "analytics-group",

    "auto.offset.reset": "earliest"
})
#offsets = consumer.offsets_for_times(partitions)
consumer.subscribe(["orders"])


import json

print("=" * 60)
print("Analytics Worker Started")
print("Reading Historical Orders...")
print("=" * 60)

while True:

    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print(msg.error())
        continue

    order = json.loads(msg.value().decode())

    print(
        f"""
Order ID : {order['order_id']}
Customer : {order['customer']}
Amount   : {order['amount']}
"""
    )