# Kafka-Inspired Messaging System Using Python Sockets

This project is a simplified, custom implementation of Apache Kafka using raw Python sockets and multi-threading. It simulates the pub-sub architecture with message brokers, partitions, producers, and consumers.

## 🧠 Key Features

- Multi-threaded broker servers simulating message partitions and offsets.
- Producers and consumers (pub.py and sub.py) communicate with brokers to send and receive messages.
- Round-robin partitioning logic across 3 brokers (`broker1`, `broker2`, `broker3`) for load distribution.
- Custom offset management for consumers to track the last message received.
- Message persistence using partition-wise flat files.



## 🧪 How It Works

1. **Start the broker servers**: Run `broker1.py`, `broker2.py`, and `broker3.py` on different terminals.
2. **Create a topic**: When a producer connects, a new topic directory is initialized with partition tracking.
3. **Publish messages**: The producer sends data, which is routed to a partition and replicated across brokers.
4. **Subscribe and consume**: The subscriber receives messages from the offset onward.

## 🛠️ Technologies Used

- Python socket programming
- Multithreading
- File I/O for partition persistence
- Round-robin logic for partition distribution

## 📌 Learning Outcome

This project helped understand the inner workings of Kafka — brokers, producers, consumers, partitions, replication, and offset-based consumption — all without using any external libraries.

## 🚀 Getting Started

1. Clone the repo
2. Start each broker script in a new terminal
3. Run `pub.py` to start publishing messages
4. Run `sub.py` to subscribe and consume

## 🧑‍💻 Contributors

- Ishani Bhat 
- Varun Avabratha
- Anirudh Koti
- Dhruva Guruprasad
## Note: Topic directories and partition files are dynamically generated when brokers and producers are executed.

