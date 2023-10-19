#!/bin/sh
# Apply database migrations
python MailingService/manage.py makemigrations app
python MailingService/manage.py migrate
# Run server
python MailingService/manage.py runserver 0.0.0.0:8000