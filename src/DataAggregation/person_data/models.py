#coding=utf-8

from django.db import models #@UnusedImport
from django.contrib.auth.models import User
from django.utils import timezone


STATUS_CHOICE = (
        (0,"未审核"),(1,"审核中"),(2,"审核通过"),(3,"审核驳回"),
    )

# Create your models here.
class User_data_service(models.Model):
    user = models.ForeignKey(User)
    service_id = models.IntegerField()
    service_name = models.CharField(max_length = 200)
    total_times = models.IntegerField(default = 0)
    call_times = models.IntegerField(default = 0)
    left_times = models.IntegerField(default = 0)
    status = models.IntegerField(choices = STATUS_CHOICE)
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)


class IP_white_list(models.Model):
    user_service = models.OneToOneField(User_data_service)
    allow_ips = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)


    
