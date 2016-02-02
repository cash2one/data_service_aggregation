#coding=utf-8
from django.db import models #@UnusedImport
from django.utils import timezone
from django.contrib.auth.models import User

USER_TYPE_CHOICE = ( (1,'个人'),(2,'企业') )
# Create your models here.
class User_Info(models.Model):
    user = models.ForeignKey(User)
    mobile_no = models.CharField(max_length=20)
    nickname = models.CharField(max_length=100)
    user_type = models.IntegerField( choices = USER_TYPE_CHOICE, default = 0 )
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)

CERTI_STATUS = (
            (0,'未审核'),(1,'审核受理中'),(2,'审核退回'),(3,'审核通过'),
    )

class User_Personal_Certi(models.Model):
    user = models.ForeignKey(User)
    realname = models.CharField(max_length=100)
    id_card_no = models.CharField(max_length=100)
    forward_side_photo = models.ImageField(upload_to='images/person/certi/',blank=True)
    back_side_photo = models.ImageField(upload_to='images/person/certi/',blank=True)
    certi_time = models.DateTimeField(default=timezone.now)
    certi_status = models.IntegerField(default = 0, choices = CERTI_STATUS) #0代表新提交，1代表审核通过，2代表审核驳回，只有被驳回的情况下才能更改
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)


class User_Org_Certi(models.Model):
    user = models.ForeignKey(User)
    company_name = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    busi_lisence_no = models.CharField(max_length=100)
    busi_lisence_photo = models.ImageField(upload_to='images/person/ico/',blank=True)
    tax_reg_no = models.CharField(max_length=100)
    tax_reg_photo = models.ImageField(upload_to='images/person/ico/',blank=True)
    org_no = models.CharField(max_length=100)
    org_photo = models.ImageField(upload_to='images/person/ico/',blank=True)
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    certi_time = models.DateTimeField(default=timezone.now)
    certi_status = models.IntegerField(default = 0, choices = CERTI_STATUS)
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)
    
    
class User_Secret(models.Model):
    user = models.ForeignKey(User)
    open_id = models.CharField(max_length=200)
    access_Key = models.CharField(max_length=200)
    create_time = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.user.username
    class Meta:
        verbose_name = u"用户秘钥"
        verbose_name_plural = verbose_name

