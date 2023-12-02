# celery.py

from celery import Celery
from celery.schedules import crontab
from my_app.tasks import my_task

app = Celery('project_name')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'my-task': {
        'task': 'my_app.tasks.my_task',
        'schedule': crontab(minute='*/1'),  # Adjust schedule as needed
    },
}
