import pika, json, time
from datetime import datetime, timedelta

def notify(task_id, status):
    c = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    ch = c.channel()
    ch.queue_declare(queue="notifier_queue", durable=True)
    ch.basic_publish(
        exchange="",
        routing_key="notifier_queue",
        body=json.dumps({"task_id": task_id, "status": status}),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    c.close()
    print("Notifier:", task_id, status)

def send_to_wait_queue(task, delay_ms):
    c  = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    ch = c.channel()
    ch.queue_declare(
        queue="wait_queue",
        durable=True,
        arguments={
            "x-dead-letter-exchange":  "",
            "x-dead-letter-routing-key": "error_queue"
        }
    )
    ch.basic_publish(
        exchange="",
        routing_key="wait_queue",
        body=json.dumps(task),
        properties=pika.BasicProperties(
            delivery_mode=2,
            expiration=str(delay_ms)  
        )
    )
    c.close()
    print(f"Sent → wait_queue (delay {delay_ms/1000:.0f}s)")

def callback(ch, method, props, body):
    task = json.loads(body)
    task_id      = task["task_id"]
    timestamp    = datetime.fromisoformat(task["timestamp"])
    first_time   = task.get("first_time", False)

    # 1️⃣ Send “in‑progress” only the first time we see this task
    if first_time:
        notify(task_id, "in-progress")
        task["first_time"] = False   # flip flag before any possible re‑queue

    # 2️⃣ Check 24‑hour rule
    if datetime.now() - timestamp >= timedelta(hours=24):
        print("Processing task:", task_id)
        time.sleep(2)                # simulate work
        notify(task_id, "completed")
    else:
        remaining = timedelta(hours=24) - (datetime.now() - timestamp)
        send_to_wait_queue(task, int(remaining.total_seconds() * 1000))

    ch.basic_ack(delivery_tag=method.delivery_tag)

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = conn.channel()
channel.queue_declare(queue="error_queue", durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="error_queue", on_message_callback=callback)

print("🎯 Error‑queue consumer listening …")
channel.start_consuming()
