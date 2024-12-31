from celery import Celery
import time

# Initialize Celery
celery = Celery(
    'tasks',
    broker='amqp://user:password@rabbitmq:5672//',
    backend='redis://redis:6379/0'
)

@celery.task(name='app.tasks.process_data')
def process_data(data):
    """
    Simulate processing data.
    """
    print(f"Processing: {data}")
    time.sleep(10)  # Simulate a long-running task
    result = f"Processed data: {data}"
    print(result)
    return result

