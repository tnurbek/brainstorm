from django.db import models
from User.models import Player

class Rating(models.Model):
    place = models.IntegerField(default=0)
    user_id = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id + ' '+ self.place


# Create your models here.
