from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Send messages to specific partitions
p.produce('my-topic', key='key1', value='Message for Consumer 1', partition=0, callback=delivery_report)
p.produce('my-topic', key='key2', value='Message for Consumer 2', partition=1, callback=delivery_report)
p.produce('my-topic', key='key3', value='Message for Consumer 3', partition=2, callback=delivery_report)

p.flush()