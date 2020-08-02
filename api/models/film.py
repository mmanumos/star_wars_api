from django.db import models
from .character import Character


class Film(models.Model):
    name = models.CharField(max_length=100)
    episode_id = models.IntegerField()
    opening_crawl = models.CharField(max_length=1200)
    director = models.CharField(max_length=120)
    producer = models.CharField(max_length=120)
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return self.name
