#coding=utf8
from django.db import models
from django.utils import timezone

# Create your models here.
class Information(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    type_name = models.CharField(max_length=100)
    info_time = models.DateField(blank=True,default=timezone.now)
    visits = models.IntegerField(blank=True,default=0)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-info_time']
        verbose_name = u"动态公告"
        verbose_name_plural = verbose_name
