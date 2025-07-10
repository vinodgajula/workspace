import pika, json

def cb(ch, method, props, body):
    print("Notifier received:", json.loads(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
ch   = conn.channel()
ch.queue_declare(queue="notifier_queue", durable=True)
ch.basic_consume(queue="notifier_queue", on_message_callback=cb)

print("🔔 Notifier listening …")
ch.start_consuming()
