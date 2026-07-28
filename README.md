# Kafka Order Processing Demo

## Overview


kafka-order-processing-demo/payment-service on  main [!?] on 🐳 v27.3.1 (desktop-linux) via payment-service via 🐍 3.8.18 took 2m 20s 
➜ docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create \
  --topic orders \
  --partitions 3 \
  --replication-factor 1


  kafka-order-processing-demo/payment-service on  main [!?] on 🐳 v27.3.1 (desktop-linux) via payment-service via 🐍 3.8.18 took 2m 20s 
➜ docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create \
  --topic payment-retry \
  --partitions 3 \
  --replication-factor 1


  kafka-order-processing-demo/payment-service on  main [!?] on 🐳 v27.3.1 (desktop-linux) via payment-service via 🐍 3.8.18 took 2m 20s 
➜ docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create \
  --topic payment-dlq \
  --partitions 3 \
  --replication-factor 1


  docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --list