import datetime

from django.db import models


class Todo(models.Model):
    WORK_STATUS = (
        ('todo', 'todo'),
        ('done', 'done'),
    )
    title = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # deadline = models.CharField(max_length=10)
    work_status = models.CharField(max_length=5, choices=WORK_STATUS, default='todo')

    def __str__(self):
        return self.title


