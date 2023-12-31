from django.db.models import Count
from rest_framework import generics, status
from .serializers import *
from rest_framework.response import Response


class ClientAPIList(generics.ListCreateAPIView):
    """Возвращает список пользователей или добавляет нового"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class FilteredClientAPIList(generics.ListAPIView):
    """Вовзращает список пользователей по тэгу и мобильному оператору"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filterset_fields = ['tag', 'mobile_operator_code']


class ClientAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вовзращает, обновляет или удаляет конкретного пользователя"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingAPIList(generics.ListCreateAPIView):
    """Возвращает список рассылок или добавляет новую"""
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MailingFullStatView(generics.RetrieveAPIView):
    """Вовзращает полную статистику конкретной рассылки"""
    queryset = Mailing.objects.annotate(
        total_messages=Count('messages')
    )
    serializer_class = MailingFullStatsSerializer


class MailingStatsList(generics.ListAPIView):
    """Возвращает список рассылок с количеством отправленных сообщений и текущим статусом"""
    queryset = Mailing.objects.annotate(
        total_messages=Count('messages')
    )
    serializer_class = MailingStatsSerializer


class CreateMessageAPIView(generics.CreateAPIView):
    """Создаёт новое сообщение по id рассылки и клиента"""
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer

    def create(self, request, *args, **kwargs):
        # Получите mailing_id и client_id из запроса
        mailing_id = request.data.get('mailing_id')
        client_id = request.data.get('client_id')

        # Попробуйте получить существующее сообщение или создать новое
        message, created = Message.objects.get_or_create(mailing_id=mailing_id, client_id=client_id)

        if created:
            # Объект был создан
            return Response({'info': 'Message created successfully.', 'id': message.id}, status=status.HTTP_201_CREATED)
        else:
            # Объект уже существует
            return Response({'info': 'Message already exists for this client and mailing.'})


class MessageAPIList(generics.ListAPIView):
    """Возвращает список сообщений"""
    queryset = Message.objects.all()
    serializer_class = MessageFullSerializer


class MessageStatusAPIView(generics.RetrieveUpdateAPIView):
    """Просматривае или обновляет статус сообщения"""
    queryset = Message.objects.all()
    serializer_class = MessageStatusSerializer
