Apache Kafka Important Commands

This document provides a list of essential Kafka commands to manage topics, producers, consumers, and monitoring.

1. Kafka Topic Management

Create a Topic

docker exec -it kafka kafka-topics --create --topic my-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1

--create → Creates a new topic.

--topic my-topic → Name of the topic.

--partitions 3 → Number of partitions.

--replication-factor 1 → Number of replicas (should be ≤ number of brokers).

List Topics

docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092

Lists all existing topics in Kafka.

Describe a Topic

docker exec -it kafka kafka-topics --describe --topic my-topic --bootstrap-server localhost:9092

Shows details of the topic like partitions, leader, and replicas.

Delete a Topic

docker exec -it kafka kafka-topics --delete --topic my-topic --bootstrap-server localhost:9092

Deletes the topic (must enable delete.topic.enable=true in Kafka settings).

2. Producing and Consuming Messages

Start a Kafka Producer

docker exec -it kafka kafka-console-producer --topic my-topic --bootstrap-server localhost:9092

Opens a prompt to send messages to my-topic.

Type messages and press Enter to send.

Start a Kafka Consumer

docker exec -it kafka kafka-console-consumer --topic my-topic --from-beginning --bootstrap-server localhost:9092

Consumes messages from my-topic.

--from-beginning → Reads all past messages.

Consume Messages in a Consumer Group

docker exec -it kafka kafka-console-consumer --topic my-topic --group my-group --bootstrap-server localhost:9092

--group my-group → Assigns the consumer to a group for load balancing.

3. Managing Consumer Groups

List Consumer Groups

docker exec -it kafka kafka-consumer-groups --bootstrap-server localhost:9092 --list

Shows all consumer groups.

Describe a Consumer Group

docker exec -it kafka kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group my-group

Displays details about the consumer group, such as offsets and partitions.

Reset Consumer Offsets

docker exec -it kafka kafka-consumer-groups --bootstrap-server localhost:9092 --group my-group --reset-offsets --to-earliest --execute

Resets the consumer offset to the earliest message in the topic.

4. Checking Kafka Cluster Health

Check Broker Status

docker exec -it kafka kafka-broker-api-versions --bootstrap-server localhost:9092

Lists supported Kafka API versions.

View Log Directories

docker exec -it kafka kafka-log-dirs --bootstrap-server localhost:9092 --describe

Shows log directory information for brokers.

Check Kafka Storage

docker exec -it kafka kafka-storage --bootstrap-server localhost:9092 --describe

Displays storage information for Kafka brokers.

5. Kafka Advanced Management

Manually Assign Partitions to Brokers

docker exec -it kafka kafka-reassign-partitions --bootstrap-server localhost:9092 --reassignment-json-file reassignment.json --execute

Moves partitions to different brokers for load balancing.

Change Topic Configurations

docker exec -it kafka kafka-configs --bootstrap-server localhost:9092 --entity-type topics --entity-name my-topic --alter --add-config retention.ms=604800000

Changes topic settings (e.g., message retention time in milliseconds).

This document serves as a quick reference for managing and using Apache Kafka efficiently.



docker pull confluentinc/cp-zookeeper:7.5.2
docker pull confluentinc/cp-kafka:7.5.2