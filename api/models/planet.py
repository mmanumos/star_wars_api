from django.db import models
from .film import Film


class Planet(models.Model):
    name = models.CharField(max_length=100)
    film = models.ForeignKey(
        Film, related_name='planets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
