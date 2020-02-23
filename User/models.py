from django.db import models
from django.contrib.auth.models import User
from Group.models import Group

class Player(User):
    # username = models.CharField(max_length=25, unique=True)
    # password = models.CharField(max_length=250)
    # first_name = models.CharField(max_length=25)
    # last_name = models.CharField(max_length=25)
    # email = models.CharField(max_length=128, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    balance = models.FloatField(default=0.0)
    country = models.CharField(max_length=25, blank=True)
    city = models.CharField(max_length=25, blank=True)
    task_n = models.IntegerField(default=0)
    team_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
