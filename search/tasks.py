# from django.contrib.auth import get_user_model
# from config import celery_app
# User = get_user_model()

# @celery_app.task()
# def get_users_count():
#     """A pointless Celery task to demonstrate usage."""
#     return User.objects.count()

from demoapp.models import Widget
from celery import shared_task
@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def count_widgets():
    return Widget.objects.count()

@shared_task
def rename_widget(widget_id, name):
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save()