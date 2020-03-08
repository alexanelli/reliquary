#!/bin/bash
#gunicorn --reload reliquary:app

export FLASK_APP=reliquary
export FLASK_ENV=development
#flask init-db
flask run
