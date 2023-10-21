from django.utils import timezone
from rest_framework import serializers
from .models import Client, Mailing, Message


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'


class MailingStatsSerializer(serializers.ModelSerializer):
    total_messages = serializers.IntegerField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Mailing
        fields = '__all__'

    def get_status(self, mailing):
        if mailing.start_time > timezone.now():
            return "Ожидает начала"
        elif mailing.end_time < timezone.now():
            return "Завершена"
        else:
            return "В процессе"


class CreateMessageSerializer(serializers.Serializer):
    mailing_id = serializers.IntegerField()
    client_id = serializers.IntegerField()


class MessageFullSerializer(serializers.ModelSerializer):
    mailing = MailingSerializer()  # Вложенный сериализатор для Mailing
    client = ClientSerializer()  # Вложенный сериализатор для Client

    class Meta:
        model = Message
        fields = '__all__'


class MessageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ['mailing', 'client', 'creation_time']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'creation_time', 'status', 'client']


class MailingFullStatsSerializer(MailingStatsSerializer):
    messages = MessageSerializer(many=True, read_only=True)
