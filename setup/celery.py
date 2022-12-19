from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.apps import apps
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
app = Celery('setup', include=['market.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])