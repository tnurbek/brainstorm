from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=25)
    content = models.CharField(max_length=2048)
    answer = models.CharField(max_length=512)
    image = models.ImageField(blank=True)

