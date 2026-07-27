import json

from confluent_kafka import Producer
from app.config.settings import settings

producer = Producer({
    "bootstrap.servers": settings.KAFKA_BOOTSTRAP_SERVERS
})


def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(
            f"✅ Delivered to topic={msg.topic()}, "
            f"partition={msg.partition()}, "
            f"offset={msg.offset()}"
        )


def publish_order(order: dict):
    print("\n========== publish_order ==========")
    print(f"Bootstrap: {settings.KAFKA_BOOTSTRAP_SERVERS}")
    print(f"Topic: {settings.ORDER_TOPIC}")
    print(f"Order: {order}")

    producer.produce(
        topic=settings.ORDER_TOPIC,
        key=order["order_id"],
        value=json.dumps(order),
        callback=delivery_report,
    )

    print("Calling flush()...")
    producer.flush()
    print("Flush complete.")