from django.contrib import admin
from .models.character import Character
from .models.film import Film
from .models.planet import Planet

# Register
admin.site.register(Character)
admin.site.register(Film)
admin.site.register(Planet)
