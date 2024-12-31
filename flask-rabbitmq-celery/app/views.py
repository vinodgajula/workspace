from flask import Flask, request, jsonify, render_template, redirect, url_for
from celery.result import AsyncResult
from app.tasks import process_data, celery  # Import the task function

app = Flask(__name__)


@app.route('/')
def index():
    """Render the HTML form for task submission."""
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def submit_task():
    """Submit a new task to the Celery worker."""
    data = request.form.get('data')  # Get form data
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Create a new task
    task = process_data.apply_async(args=[data])
    return redirect(url_for('task_status', task_id=task.id))  # Redirect to status page


@app.route('/status/<task_id>')
def task_status(task_id):
    """Render the task status page."""
    return render_template('status.html', task_id=task_id)


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    """Fetch the result of a specific task."""
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
    """Cancel a specific task."""
    result = AsyncResult(task_id, app=celery)
    if result.status in ["PENDING", "STARTED"]:
        celery.control.revoke(task_id, terminate=True)
        return jsonify({"message": f"Task {task_id} has been cancelled."})
    return jsonify({"message": f"Task {task_id} cannot be cancelled.", "status": result.status})

