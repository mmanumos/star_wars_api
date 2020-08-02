import graphene
from graphene_django.types import DjangoObjectType
from .models.character import Character
from .models.film import Film
from .models.planet import Planet
from graphene import ObjectType

""" Define types for queries """


class CharacterType(DjangoObjectType):
    """ Type to define queries and mutations using the model Character """
    class Meta:
        model = Character


class FilmType(DjangoObjectType):
    """ Type to define queries and mutations using the model Film """
    class Meta:
        model = Film


class PlanetType(DjangoObjectType):
    """ Type to define queries and mutations using the model Planet """
    class Meta:
        model = Planet


""" QUERIES """


class Query(object):
    # Queries for Characters
    character = graphene.Field(CharacterType, id=graphene.Int(
    ), name=graphene.String(), height=graphene.Int(), mass=graphene.Int(), gender=graphene.String())
    all_characters = graphene.List(CharacterType)

    def resolve_character(self, info, **kwargs):
        """ Query to get character by attribute """
        id = kwargs.get('id')
        name = kwargs.get('name')
        height = kwargs.get('height')
        mass = kwargs.get('mass')
        gender = kwargs.get('gender')

        if id is not None:
            return Character.objects.get(id=id)
        if name is not None:
            return Character.objects.get(name=name)
        if height is not None:
            return Character.objects.get(height=height)
        if mass is not None:
            return Character.objects.get(mass=mass)
        if gender is not None:
            return Character.objects.get(gender=gender)
        return None

    def resolve_all_characters(self, info, **kwargs):
        """ Query to get all characters """
        return Character.objects.all()

    # Queries for Films
    film = graphene.Field(FilmType, id=graphene.Int(),
                          name=graphene.String(),
                          episode_id=graphene.Int(),
                          director=graphene.String(),
                          producer=graphene.String()
                          )
    all_films = graphene.List(FilmType)

    def resolve_film(self, info, **kwargs):
        """ Query to get film by attribute """
        id = kwargs.get('id')
        episode_id = kwargs.get('episode_id')
        director = kwargs.get('director')
        producer = kwargs.get('producer')

        if id is not None:
            return Film.objects.get(id=id)
        if episode_id is not None:
            return Film.objects.get(episode_id=episode_id)
        if director is not None:
            return Film.objects.get(director=director)
        if producer is not None:
            return Film.objects.get(producer=producer)
        return None

    def resolve_all_films(self, info, **kwargs):
        """ Query to get all films """
        return Film.objects.all()

    # queries to planets
    planet = graphene.Field(
        PlanetType, name=graphene.String())
    all_planets = graphene.List(PlanetType)

    def resolve_all_planets(self, info, **kwargs):
        return Planet.objects.select_related('film').all()
