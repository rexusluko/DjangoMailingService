FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /MailingService

COPY requirements.txt /MailingService/
RUN pip install -r requirements.txt

COPY . /MailingService/