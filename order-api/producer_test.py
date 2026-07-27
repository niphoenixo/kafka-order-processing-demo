from confluent_kafka import Producer

producer = Producer({
    "bootstrap.servers": "localhost:29092"
})

producer.produce("orders", key="1", value="Hello Kafka")
producer.flush()

print("Done")