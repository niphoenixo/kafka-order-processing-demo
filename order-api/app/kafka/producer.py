import json

from confluent_kafka import Producer

from app.config.settings import settings


producer = Producer({
    "bootstrap.servers": settings.KAFKA_BOOTSTRAP_SERVERS
})


def publish_order(order: dict):
    producer.produce(
        topic=settings.ORDER_TOPIC,
        key=order["order_id"],
        value=json.dumps(order)
    )

    producer.flush()