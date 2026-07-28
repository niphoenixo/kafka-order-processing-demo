import os

from confluent_kafka import Consumer
from dotenv import load_dotenv

load_dotenv()

consumer = Consumer({
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    "group.id": "replay-worker-group",
    "auto.offset.reset": "earliest"
})

consumer.subscribe([os.getenv("DLQ_TOPIC")])