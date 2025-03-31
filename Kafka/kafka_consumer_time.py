from confluent_kafka import Consumer, KafkaError, KafkaException

# Consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    'group.id': 'my-consumer-group',        # Consumer group ID
    'auto.offset.reset': 'earliest'         # Start reading from the beginning of the topic if no offset is stored
}

# Create a consumer instance
consumer = Consumer(conf)

# Subscribe to the topic
topic = 'my-topic'
consumer.subscribe([topic])

# Poll for messages
try:
    while True:
        # Poll for a message (timeout in seconds)
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            # No message received within the timeout period
            continue

        if msg.error():
            # Handle errors
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event (not an error)
                print(f"Reached end of partition {msg.partition()} at offset {msg.offset()}")
            elif msg.error():
                # Other errors
                raise KafkaException(msg.error())
        else:
            # Safely handle None keys and values
            key = msg.key().decode('utf-8') if msg.key() else None
            value = msg.value().decode('utf-8') if msg.value() else None

            # Get the message timestamp
            timestamp_type, timestamp = msg.timestamp()
            if timestamp_type == 0:  # TimestampType.NOT_AVAILABLE
                timestamp_str = "Not available"
            else:
                # Convert timestamp to a human-readable format
                from datetime import datetime
                timestamp_str = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

            # Print the received message
            print(f"Received message: key={key}, value={value}, partition={msg.partition()}, offset={msg.offset()}, timestamp={timestamp_str}")

except KeyboardInterrupt:
    # Allow the user to stop the consumer with Ctrl+C
    print("Consumer stopped by user.")

finally:
    # Close the consumer gracefully
    consumer.close()