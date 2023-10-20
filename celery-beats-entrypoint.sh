#!/bin/sh
cd ./MailingService
celery -A MailingService beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler