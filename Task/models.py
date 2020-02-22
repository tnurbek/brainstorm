from django.db import models
from Level.models import Level


class Task(models.Model):
    name = models.CharField(max_length=25)
    content = models.CharField(max_length=2048)
    answer = models.CharField(max_length=512)
    image = models.ImageField(blank=True)
    level_id = models.ForeignKey(on_delete=models.CASCADE)


    def __str__(self):
        return self.name



