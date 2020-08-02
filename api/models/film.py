from django.db import models
from .character import Character
from .planet import Planet


class Film(models.Model):
    name = models.CharField(max_length=100)
    episode_id = models.IntegerField(null=True)
    opening_crawl = models.CharField(max_length=1200, null=True)
    director = models.CharField(max_length=120, null=True)
    producer = models.CharField(max_length=120, null=True)
    characters = models.ManyToManyField(Character)
    planets = models.ManyToManyField(Planet)

    def __str__(self):
        return self.name
