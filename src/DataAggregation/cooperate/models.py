#coding=utf8
from django.db import models
from django.utils import timezone

# Create your models here.
class MessageBoard(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(blank=True, max_length=11)
    messagecontent = models.TextField(max_length=1000)
    msg_time = models.DateTimeField(null=True,blank=True,default=timezone.now)
    class Meta:
        verbose_name = u"留言板"
        verbose_name_plural = verbose_name