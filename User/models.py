from django.db import models
from django.contrib.auth.models import User
from Group.models import Group

class Player(User):
    phone = models.CharField(max_length=15, unique=True)
    balance = models.FloatField(default=0.0)
    country = models.CharField(max_length=25, blank=True)
    city = models.CharField(max_length=25, blank=True)
    task_n = models.IntegerField(default=0)
    team_id = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username + self.first_name
