from celery import shared_task
from celery.schedules import crontab

from .models import *
import requests

@shared_task
def send_request_to_url():
    url = "https://web:8000/api/v1/mailings/stats"
    response = requests.get(url)
    print(f'Response from {url}: {response.text}')
