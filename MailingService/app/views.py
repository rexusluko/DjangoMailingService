from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.

class ClientAPIList(generics.ListCreateAPIView):
    """Возвращает список пользователей или добавляет нового"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вовзращает, обновляет или удаляет конкретного пользователя"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class MailingAPIList(generics.ListCreateAPIView):
    """Возвращает список рассылок или добавляет новую"""
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

class MailingAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вовзращает, обновляет или удаляет конкретную рассылку"""
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

class MailingStatsView(generics.ListAPIView):
    '''Возвращает список рассылок с количеством отправленных сообщений'''
    queryset = Mailing.objects.annotate(
        total_messages=Count('message')
    )
    serializer_class = MailingStatSerializer
