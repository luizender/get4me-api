# API Rest Project of Get4me

This project is an API to the Get4me solution generated at the event Intelbras LAB.

## Table of Contents

* [Requirements](#requirements)
* [Setup](#setup)
* [Running](#running)
* [Running with Shell](#running-with-shell)
* [Access the API](#access-the-api)

## Requirements

This project can be executed in several operation system (SO), but has the following dependencies:
* [Django](https://www.djangoproject.com/) == 1.11.11
* [Djangorestframework](http://www.django-rest-framework.org/) == 3.8.2
* [Mysqlclient](https://mysqlclient.readthedocs.io/) == 1.3.13
* [Python](https://www.python.org/) >= 3
* [Pip](http://www.pip-installer.org/en/latest/)

## Setup

To set up the containers, you need to execute

```
docker-compose build
```

This command will build two containers: one container for api and the another container for database

## Running

To run the containers, you need to execute

```
docker-compose up
```

This command will run the database and the API.

## Running with Shell

To run with shell, you need to execute

```
docker-compose run --service-ports api sh
```

After that, you need to execute the follow command to start the API

```
make run
```

## Access the API

You can access the API using the follow step:

```
curl -X GET http://127.0.0.1:8000/
```

Or, you can access using your browser with the address ```http://127.0.0.1:8000/```
