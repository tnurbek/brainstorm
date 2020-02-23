from django.db import models
from User.models import Player
from datetime import datetime

class Finisher(models.Model):
    finished_time = models.DateTimeField()
    user_id = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id + ' '+ self.finished_time



# Create your models here.
