from django.db import models
from Task.models import Task
from datetime import datetime

class Completed_task(models.Model):
    finished = models.DateTimeField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)



