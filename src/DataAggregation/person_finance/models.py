#coding=utf-8
from django.db import models #@UnusedImport
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Bank_account_info(models.Model):
    bank_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)
    score = models.IntegerField()
    def __unicode__(self):
        return self.account
    class Meta:
        verbose_name = u"收款银行账户"
        verbose_name_plural = verbose_name


class Alipay_account_info(models.Model):
    company_name = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)
    score = models.IntegerField()  
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.account
    class Meta:
        verbose_name = u"收款支付宝账户"
        verbose_name_plural = verbose_name
        

class User_account(models.Model):
    user = models.OneToOneField(User)
    money = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)


class User_DM_account(models.Model):
    user = models.OneToOneField(User)
    coins = models.IntegerField(default = 0)
    free_coins = models.IntegerField(default = 0)
    pay_coins = models.IntegerField(default = 0)
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)


class DM_Charge_type(models.Model):
    type_name = models.CharField(max_length = 30)
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.type_name
    
    
class User_DM_charge_log(models.Model):
    user = models.ForeignKey(User)
    charge_type = models.ForeignKey(DM_Charge_type , default = 1)
    coins = models.IntegerField(default = 0)
    coins_before = models.IntegerField(default = 0)
    coins_after = models.IntegerField(default = 0)
    free_coins_before = models.IntegerField(default = 0)
    free_coins_after = models.IntegerField(default = 0)
    pay_coins_before = models.IntegerField(default = 0)
    pay_coins_after = models.IntegerField(default = 0)
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)


class DM_Cost_type(models.Model):
    type_name = models.CharField(max_length = 30)
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.type_name
    
        
class User_DM_cost_log(models.Model):
    user = models.ForeignKey(User)
    cost_type = models.ForeignKey(DM_Cost_type, default = 1)
    coins = models.IntegerField(default = 0)
    coins_before = models.IntegerField(default = 0)
    coins_after = models.IntegerField(default = 0)
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)
    
    
ALARM_STATUS_CHOICE = (
                (0, '关闭'),(1, '开启'),
        )

class User_account_alarm(models.Model):
    user = models.OneToOneField(User)
    account = models.ForeignKey(User_account);
    alarm_line = models.IntegerField(default=100)
    alarm_status = models.IntegerField(choices=ALARM_STATUS_CHOICE,default=0)#使用get_alarm_status_display做choices显示，xx字段即为get_xx_display
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)
    

class Charge_type(models.Model):
    type_name = models.CharField(max_length = 30)
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.type_name
    

class Charge_normal_logs(models.Model):
    user = models.ForeignKey(User)
    account = models.ForeignKey(User_account);
    charge_type = models.ForeignKey(Charge_type,default = 1)
    serve_base_id = models.IntegerField(blank=True,)
    serve_pack_id = models.IntegerField(blank=True,)
    number_of_pack = models.IntegerField(blank=True,default = 1)
    charge_money = models.DecimalField(max_digits=10, decimal_places=2 )
    money_before = models.DecimalField(max_digits=10, decimal_places=2 )
    money_after = models.DecimalField(max_digits=10, decimal_places=2 )
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)

    
class Cost_type(models.Model):
    type_name = models.CharField(max_length = 30)
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.type_name
    
    
class Cost_normal_logs(models.Model):
    user = models.ForeignKey(User)
    account = models.ForeignKey(User_account)
    cost_type = models.ForeignKey(Cost_type ,default = 2)
    cost_money = models.DecimalField(max_digits=10, decimal_places=2 )
    money_before = models.DecimalField(max_digits=10, decimal_places=2 )
    money_after = models.DecimalField(max_digits=10, decimal_places=2 )
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)
    
    
COUPON_USED = (
                (0, '未使用'),(1, '已使用'),
        )        
    
class User_coupon(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000)
    discount = models.DecimalField(max_digits=2, decimal_places=1 )
    limit_date = models.DateField(default=timezone.now)
    limit_times = models.IntegerField()
    used = models.IntegerField(default = 0 , choices = COUPON_USED)
    create_time = models.DateTimeField(default=timezone.now)
    modify_time = models.DateTimeField(default=timezone.now)


