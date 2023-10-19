#!/bin/sh
cd ./MailingService
celery -A MailingService worker -l info