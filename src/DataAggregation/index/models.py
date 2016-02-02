#coding=utf8
from django.db import models

# Create your models here.
class Search_Words(models.Model):
    word = models.CharField(max_length=200)
    visits = models.IntegerField(default=1)
    def __unicode__(self):
        return self.words
    class Meta:
        ordering = ['-visits']
        verbose_name = u"热门搜索"
        verbose_name_plural = verbose_name