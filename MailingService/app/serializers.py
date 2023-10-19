from django.utils import timezone
from rest_framework import serializers
from .models import Client, Mailing



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'


class MailingStatSerializer(serializers.ModelSerializer):
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