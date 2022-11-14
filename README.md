# django-starting-project

This project is the development of the OpenClassrooms tutorial: [Débutez avec le framework Django](https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django)


The only difference is that I didn't use venv + sqlite, but two containers: a python container and a postgresql container created using docker (dockerfile and docker compose)

As I have always worked with gitlab, I also took the opportunity to set up a **github action** to run **pylint django**. The idea was not to have a good or bad score, just to see how the github actions work. Now there is an action running pylint django every time I push something new here.

How to use this project?
* __git clone__
* __docker compose up__ (you need the docker daemon running)
* open a shell attached to django container and apply migrations: __./manage.py migrate__
* open localhost in your fav browser or click here : __http://localhost:8000/__
