#!/bin/sh
python MailingService/manage.py makemigrations app
# Ожидание доступности базы данных
sleep 15
# Применение миграций
python MailingService/manage.py migrate

# Запуск Django приложения
python MailingService/manage.py runserver 0.0.0.0:8000