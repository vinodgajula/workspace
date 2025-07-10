import pika, json, uuid
from datetime import datetime, timedelta

past_time = datetime.now() - timedelta(hours=23, minutes=59)

task = {
    "task_id": str(uuid.uuid4()),
    "message": "Do something important",
    #"timestamp": datetime.now().isoformat(),
    "timestamp": past_time.isoformat(),  # ⬅️ Use backdated time
    "first_time": True          # <── flag to know if we’ve notified “in‑progress”
}

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
ch   = conn.channel()
ch.queue_declare(queue="error_queue", durable=True)

ch.basic_publish(
    exchange="",
    routing_key="error_queue",
    body=json.dumps(task),
    properties=pika.BasicProperties(delivery_mode=2)
)

print("Sent task → error_queue:", task)
conn.close()
