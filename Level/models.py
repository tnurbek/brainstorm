from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=25)
    duration = models.IntegerField()

    def __str__(self):
        return self.name
