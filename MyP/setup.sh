#!/bin/bash

# Install dependencies
pip install setuptools
pip install -r requirements

# Run Django commands
python manage.py makemigrations
python manage.py migrate
python manage.py tailwind install
python manage.py collectstatic --noinput
python manage.py tailwind start