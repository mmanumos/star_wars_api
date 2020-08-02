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

    # queries to planets
    planet = graphene.Field(
        PlanetType, id=graphene.Int(), name=graphene.String())
    all_planets = graphene.List(PlanetType)

    def resolve_planet(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Planet.objects.get(id=id)
        if name is not None:
            return Planet.objects.get(name=name)

    def resolve_all_planets(self, info, **kwargs):
        return Planet.objects.all()


""" MUTATIONS """


# customized data inputs for Film (lists -> ManyToMany)
class CharacterData(graphene.InputObjectType):
    """ Data input for Character """
    name = graphene.String(required=True)
    height = graphene.Int()
    mass = graphene.Int()
    gender = graphene.String()

# customized data inputs for Film (lists -> ManyToMany)


class PlanetData(graphene.InputObjectType):
    """ Data input for Planet """
    name = graphene.String(required=True)


class CreateFilm(graphene.Mutation):
    """ Create Film """
    class Arguments:
        name = graphene.String(required=True)
        episode_id = graphene.Int()
        opening_crawl = graphene.String()
        director = graphene.String()
        producer = graphene.String()
        characters_list = graphene.List(CharacterData)
        planets_list = graphene.List(PlanetData)

    film = graphene.Field(FilmType)

    def mutate(self, info, name, episode_id=None, opening_crawl=None,
               director=None, producer=None, characters_list=None, planets_list=None):
        """ Setting data with info """
        obj = Film.objects.create(name=name, episode_id=episode_id,
                                  opening_crawl=opening_crawl, director=director, producer=producer)
        # Creating and associating characters to new film
        if characters_list is not None:
            for char_data in characters_list:
                obj_sub = Character.objects.create(
                    name=char_data.name, height=char_data.height, mass=char_data.mass, gender=char_data.gender)
                obj.characters.add(obj_sub)

        # Creating and associating characters to new film
        if planets_list is not None:
            for plan_data in planets_list:
                obj_sub = Planet.objects.create(name=plan_data.name)
                obj.planets.add(obj_sub)

        return CreateFilm(film=obj)


class UpdateFilm(graphene.Mutation):
    """ Update film """
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        episode_id = graphene.Int()
        opening_crawl = graphene.String()
        director = graphene.String()
        producer = graphene.String()

    film = graphene.Field(FilmType)

    def mutate(self, info, id, name=None, episode_id=None, opening_crawl=None, director=None, producer=None):
        try:
            obj = Film.objects.get(id=id)
            obj.name = name
            obj.episode_id = episode_id
            obj.opening_crawl = opening_crawl
            obj.director = director
            obj.producer = producer
            obj.save()
            return UpdateFilm(film=obj)
        except Exception:
            return None


class CreateCharacter(graphene.Mutation):
    """ Create Character """
    class Arguments:
        character_data = graphene.Argument(CharacterData)

    character = graphene.Field(CharacterType)

    def mutate(self, info, character_data):
        """ Setting data with info """
        obj = Character()
        for key, value in character_data.items():
            setattr(obj, key, value)
            obj.save()
        return CreateCharacter(character=obj)


class UpdateCharacter(graphene.Mutation):
    """ Update Character """
    class Arguments:
        id = graphene.Int()
        character_data = graphene.Argument(CharacterData)

    character = graphene.Field(CharacterType)

    def mutate(self, info, id, character_data):
        """ Setting data with info """
        try:
            obj = Character.objects.get(id=id)
            for key, value in character_data.items():
                setattr(obj, key, value)
            obj.save()
            return UpdateCharacter(character=obj)
        except Exception:
            return None


class CreatePlanet(graphene.Mutation):
    """ Create Planet """
    class Arguments:
        name = graphene.String(required=True)

    planet = graphene.Field(PlanetType)

    def mutate(self, info, name):
        obj = Planet.objects.create(name=name)
        return CreatePlanet(planet=obj)


class UpdatePlanet(graphene.Mutation):
    """ Update planet """
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    planet = graphene.Field(PlanetType)

    def mutate(self, info, id, name):
        try:
            obj = Planet.objects.get(id=id)
            obj.name = name
            obj.save()
            return UpdatePlanet(planet=obj)
        except Exception:
            return None


class Mutation(ObjectType):
    """ mutations register """
    create_film = CreateFilm.Field()
    update_film = UpdateFilm.Field()
    create_character = CreateCharacter.Field()
    update_character = UpdateCharacter.Field()
    create_planet = CreatePlanet.Field()
    update_planet = UpdatePlanet.Field()
