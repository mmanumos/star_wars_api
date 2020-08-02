from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    mass = models.IntegerField()
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name
