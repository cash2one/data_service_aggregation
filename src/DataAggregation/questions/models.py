#coding=utf8
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Question_Type(models.Model):
    type_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.type_name
    class Meta:
        verbose_name = u"问题分类"
        verbose_name_plural = verbose_name


class Question_Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    visits = models.IntegerField(blank=True,default=0)
    def __unicode__(self):
        return self.tag_name
    class Meta:
        verbose_name = u"问题标签"
        verbose_name_plural = verbose_name


class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    quest_time = models.DateTimeField(blank=True,default=timezone.now)
    lastest_anwser_time = models.DateTimeField(blank=True,default=timezone.now)
    visits = models.IntegerField(blank=True,default=0)
    tags = models.ManyToManyField(Question_Tag)
    user = models.ForeignKey(User)
    type = models.ForeignKey(Question_Type)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-lastest_anwser_time']
        verbose_name = u"问题"
        verbose_name_plural = verbose_name

        
class Anwser(models.Model):
    description = models.CharField(max_length=1000)
    anwser_time = models.DateTimeField(blank=True,default=timezone.now)
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    def __unicode__(self):
        return self.description
    class Meta:
        ordering = ['id']
        verbose_name = u"回答"
        verbose_name_plural = verbose_name
