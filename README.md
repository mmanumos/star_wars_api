# Star Wars - API

API desarrollada bajo la estrucura de datos del universo de STAR WARS implementada en el sitio https://swapi.dev/  
Para esta versión el usuario puede listar personajes, cada personaje puede ver las películas en las que participa,
cada película permite ver detalles como el texto apertura, los planetas, el director y los productores.

## Entorno de desarrollo

* [x]  Sistema operativo Ubuntu 20.04 LTS
* [x]  Motor de bases de datos sqlite 3.31.1
* [x]  Python 3.8.2


## Stack Tecnológico

* [x] GraphQL como lenguaje de manipulación y consulta de datos.
* [x] Django 3.0.8
* [x] graphene 2.1.8

* Para instalación visite la documentación
    https://docs.graphene-python.org/projects/django/en/latest/


## La aplicación funciona de la siguiente manera:

### 1ro 
- Abrir una terminal y ubicarse en la carpeta raíz de la aplicación "star_wars_api". 
  Ejecutar el comando: python3 manage.py runserver

### 2do
- En el navegador digitar la url: http://localhost:8000/graphql/ este lo dirigirá al explorador Graphiql.
- En el explorador puede hacer uso de algunas queries y mutations guardadas en el archivo "star_wars.json" ubicado
  en el directorio raíz de la API.


