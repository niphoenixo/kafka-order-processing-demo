import os

from confluent_kafka import Consumer
from dotenv import load_dotenv

load_dotenv()


def create_consumer(group_id: str):

    return Consumer({
        "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
        "group.id": group_id,
        "auto.offset.reset": "earliest"
    })