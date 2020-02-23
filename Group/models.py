from django.db import models
from django.contrib.auth.models import Group
from Task.models import Task
from Option.models import Option

class Group(Group):
    money = models.IntegerField()
    start = models.TimeField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    option_id = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
