# RESTAPi project


## Opportunities 

The project presents an API where Token authorization is implemented, the user can create a world recipe with ingredients, tags, and you can also upload photos to them. This REST API uses CRUD operations.

### Technology

Python, Django, Django Rest Framework, PostgreSQL, Test Drive Development, AWS

### Use the following commands to run docker-compose on your computer or if you want run AWS server open deployment.md file:

```sh
docker-compose up
```

### Run test and flake8
```sh
docker-compose run --rm app sh -c "python manage.py test && flake8"
```