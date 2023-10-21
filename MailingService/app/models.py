from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.utils import timezone


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, unique=True)  # Номер телефона в формате +7XXXXXXXXXX
    mobile_operator_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=255)  # Произвольная метка
    timezone = models.CharField(max_length=50)  # Часовой пояс

    def __str__(self):
        return self.phone


# Create your models here.
class Mailing(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(blank=False, null=False)
    text = models.CharField(blank=False, null=False)
    mobile_operator_filter = models.CharField(max_length=3, null=True)
    tag_filter = models.CharField(max_length=255, null=True)
    end_time = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    creation_time = models.DateTimeField(default=timezone.now,blank=False, null=False)
    status = models.CharField(default="Не отправлено",blank=False, null=False)
    mailing = models.ForeignKey(Mailing, related_name='messages',on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
