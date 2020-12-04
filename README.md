# app-ayomi
réalisation test technique pour Ayomi

# Init github app-ayomi
`git clone https://github.com/BCouble/app-ayomi.git`

# Init Docker

- Django & PostgreSql
link
https://docs.docker.com/engine/examples/postgresql_service/

Create file :
    - DockerFiles
    - docker-compose.yml

Build an image from the Dockerfile and assign it a name.

`docker-compose run web django-admin startproject ayomi .`

- result : WARNING: Image for service web was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.

- Settings.py update DATABASES

`docker-compose up`

-  Create venv
`python -m venv venv`

-  Activate venv
`venv\Scripts\activate.bat`

Create folders for apps
Create app core for template

`python manage.py startapp core ./ayomi/apps/core`

Create app register for user management

`python manage.py startapp register ./ayomi/apps/register`

Create template folder and files

Update setting file for 'DIRS' in TEMPLATES

Import static file in core :
bootstrap sb-admin-2

Create html file & import css & js

Create superuser
docker-compose run web python manage.py createsuperuser


