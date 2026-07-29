
## ⭐ Useful Commands

## 1️ List all topics

```bash
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --list
```

---

## 2️ Describe a topic (Partitions, Leader, Replicas, ISR)

Replace `orders` with any topic name.

```bash
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --describe \
  --topic orders
```

---

## 3️ Read messages with Offset and Key ⭐

This is my favourite debugging command.

```bash
docker exec -it kafka /opt/kafka/bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic orders \
  --from-beginning \
  --property print.offset=true \
  --property print.key=true
```

---

## 4️ Show Consumer Group details (Offset & Lag) ⭐⭐⭐

Replace `payment-group` with any consumer group.

```bash
docker exec -it kafka /opt/kafka/bin/kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --describe \
  --group payment-group
```

This shows:

* Current Offset
* Log End Offset
* Lag
* Consumer ID
* Host

---

## 5️ Show all Consumer Groups

```bash
docker exec -it kafka /opt/kafka/bin/kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --list
```

---



## 6 Create a topic

```bash
 docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create \
  --topic orders \
  --partitions 3 \
  --replication-factor 1


 docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create \
  --topic payment-retry \
  --partitions 3 \
  --replication-factor 1


  docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create \
  --topic payment-dlq \
  --partitions 3 \
  --replication-factor 1
```

---

## 7 Read only Partition 0

```bash
docker exec -it kafka /opt/kafka/bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic orders \
  --partition 0 \
  --from-beginning \
  --property print.offset=true \
  --property print.key=true
```