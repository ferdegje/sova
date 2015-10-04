# sova
# This repository contains the artifacts to build the SOVA project

<h1>API</h1>
This folder contains the Python code for the API

<h2>Setup</h2>
- cd api
- virtualenv venv
- pip install -r requirements.txt
- Open PyCharm
- File > Open...
- Select sova/api
- Create a new Configuration for the script run.py

<h2>First Steps</h2>
- Start by running the server, either through Pycharm or just run python run.py within the virtualenv
- Open Postman
- Create a super user:
-- Make a POST request to http://localhost/accounts with a payload of {"username": "super", "password": "social101", "roles": ["superuser","user"]} (currently, you also need to put an Authorization of Basic Auth with imaginary username and passwords, that needs to be sorted)
- You can now:
-- Query the API: GET http://localhost/accounts with username super and password social101
-- Query more of the API: GET http://localhost/people with username super and password social101
-- Create objects in the API: POST http://localhost/people [{"firstname": "barack", "lastname": "obama"}, {"firstname": "mitt", "lastname": "romney"}] with username super and password social101
-- Query the API again: GET http://localhost/people with username super and password social101
-- Add your own API endpoints:
--- add a file in the models directory (for example cars.py), copying from people.py
--- add an import statement in settings.py. Following our previous example, add from models.cars import cars
--- add an entry into the DOMAIN dictionary, 'cars': cars
