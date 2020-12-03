# app-ayomi
réalisation test technique pour Ayomi

# Init github app-ayomi
git clone https://github.com/BCouble/app-ayomi.git

# Init Docker

- Django & PostgreSql
link
https://docs.docker.com/engine/examples/postgresql_service/

Create file :
    - DockerFiles
    - stack.yml

Build an image from the Dockerfile and assign it a name.

...

docker-compose run web django-admin startproject ayomi .

...
result : WARNING: Image for service web was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.

Settings.py update DATABASES
