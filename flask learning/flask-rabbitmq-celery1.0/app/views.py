from flask import Flask, request, jsonify
from celery.result import AsyncResult
from .tasks import celery

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_task():
    data = request.json
    task = celery.send_task('app.tasks.process_data', args=[data])
    return jsonify({"task_id": task.id, "status": "Task Submitted"}), 202
@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    result = AsyncResult(task_id, app=celery)
    response = {
        "task_id": task_id,
        "status": result.status,
    }
    if result.status == "SUCCESS":
        response["result"] = result.result
    elif result.status == "FAILURE":
        response["error"] = str(result.result)
    else:
        response["result"] = "Task is still being processed"
    return jsonify(response)

@app.route('/cancel/<task_id>', methods=['POST'])
def cancel_task(task_id):
    result = AsyncResult(task_id, app=celery)
    if result.status in ["PENDING", "STARTED"]:
        celery.control.revoke(task_id, terminate=True)
        return jsonify({"message": f"Task {task_id} has been cancelled."})
    return jsonify({"message": f"Task {task_id} cannot be cancelled.", "status": result.status})
