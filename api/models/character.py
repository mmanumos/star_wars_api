from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    height = models.IntegerField(null=True)
    mass = models.IntegerField(null=True)
    gender = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
