from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

"""
Configuration taken from:
http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'funwithcelery.settings')

app = Celery('funwithcelery')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
