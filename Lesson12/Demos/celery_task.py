# tasks.py

from celery import Celery
import time

celery = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@celery.task
def long_task():
    """
    Simulates a long-running task.
    """
    total = 25
    for i in range(total):
        time.sleep(1)
    return 'Task completed!'