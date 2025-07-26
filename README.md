# Kafka-Inspired Messaging System Using Python Sockets

This project is a simplified, custom implementation of Apache Kafka using raw Python sockets and multi-threading. It simulates the pub-sub architecture with message brokers, partitions, producers, and consumers.

## 🧠 Key Features

- Multi-threaded broker servers simulating message partitions and offsets.
- Producers and consumers (pub.py and sub.py) communicate with brokers to send and receive messages.
- Round-robin partitioning logic across 3 brokers (`broker1`, `broker2`, `broker3`) for load distribution.
- Custom offset management for consumers to track the last message received.
- Message persistence using partition-wise flat files.



