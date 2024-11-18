# To run this app, execute the following command in the terminal:
# Setup Redis and Celery and start the services in terminal
# run redis-server after installing redis (pip install redis)
# run celery -A celery_task worker --loglevel=info after installing celery (pip install celery)

from flask import Flask, url_for, jsonify
from flask_socketio import SocketIO
import os
from dotenv import load_dotenv
from celery import Celery

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Configure Celery with Redis as the message broker and result backend
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'  # Using Redis database 0
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Import tasks
from celery_task import long_task

# Initialize SocketIO
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/start-task', methods=['POST'])
def start_task():
    """
    Starts the long-running Celery task.
    """
    # Start the Celery task
    task = long_task.apply_async(args=[])
    # Return the task ID to the client
    return jsonify({'task_id': task.id}), 202, {'Location': url_for('task_status', task_id=task.id)}

@app.route('/status/<task_id>')
def task_status(task_id):
    """
    Retrieves the status of a Celery task.
    """
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        # Task is pending
        response = {
            'state': task.state,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        # Task is processing or completed
        response = {
            'state': task.state,
            'status': task.info  # Can be None
        }
        if task.state == 'SUCCESS':
            response['result'] = task.result
    else:
        # Task failed
        response = {
            'state': task.state,
            'status': str(task.info)  # Exception info
        }
    return jsonify(response)

@app.route('/')
def index():
    """
    Home page with instructions.
    """
    return '''
    <h1>Flask Celery Demo</h1>
    <p>Use the /start-task endpoint to start a background task.</p>
    <p>Example:</p>
    <pre>
    curl -X POST http://localhost:5000/start-task
    </pre>
    '''

# --------------------
# Run the Flask app
# --------------------

if __name__ == '__main__':
    socketio.run(app)