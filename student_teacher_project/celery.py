import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_teacher_project.settings')

app = Celery('student_teacher_project', backend='redis', broker='redis://localhost:6379')

app.config_from_object('django.conf:settings',  namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))