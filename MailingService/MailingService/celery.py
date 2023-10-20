import os
from datetime import datetime

from celery import Celery
from celery.schedules import crontab
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MailingService.settings')

app = Celery('MailingService')
app.config_from_object('django.conf:settings', namespace='CELERY')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, send_messages.s(), expires=10, name='send messages')


@app.task
def test(arg):
    print(arg)


@app.task
def add(x, y):
    z = x + y
    print(z)


@app.task
def send_messages():
    stat_url = "http://web:8000/api/v1/mailings/stats"
    stat_response = requests.get(stat_url)  # Получение статистики по рассылкам

    if stat_response.status_code != 200:  # Проверка успешности запроса
        print(f"Status Request failed with status code: {stat_response.status_code}")
        return
    stat_json_data = stat_response.json()  # Получение JSON-данных из ответа
    current_mailings = []
    for mailing in stat_json_data: # Отбор активных рассылок
        if mailing['status'] == 'В процессе':
            current_mailings.append((mailing['id'], mailing['mobile_operator_filter'], mailing['tag_filter']))
    print(current_mailings)
    for mailing_id, mobile_operator, tag in current_mailings:
        filtred_clients_url = f'http://web:8000/api/v1/clients/filter/?tag={tag}&mobile_operator_code={mobile_operator}'
        filtred_clients_response = requests.get(filtred_clients_url)

        if filtred_clients_response.status_code != 200:  # Проверка успешности запроса
            print(f"Filtred Clients Request failed with status code: {filtred_clients_response.status_code}")
            return
        filtred_clients_json_data =  filtred_clients_response.json()  # Получение JSON-данных из ответа
        for client in filtred_clients_json_data:
            create_message_url = "http://web:8000/api/v1/messages/create/"
            requests.post(create_message_url,data={'mailing_id': mailing_id,'client_id': client['id']})
