import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from graphene.test import Client
# Models
from api.models.film import Film
from api.models.character import Character
from api.models.planet import Planet
from star_wars_api.schema import schema


single_film_query = """ 
    query($id:Int)
    {
        film(id:$id){
            id,
            name
        }
    }
 """


@pytest.mark.django_db
class TestApiSchema(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.film = mixer.blend(Film)

    def test_single_film_query(self):
        response = self.client.execute(
            single_film_query, variable_values={"id": self.film.id})
        response_film = response.get("data").get("film")
        assert response_film["id"] == str(self.film.id)
