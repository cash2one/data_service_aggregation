#coding=utf-8
from django.db import models
from django.utils import timezone

# Create your models here.
class S_Province(models.Model):
    ProvinceID = models.AutoField("ProvinceID",primary_key=True)
    ProvinceName = models.CharField(max_length=100)
    DateCreated = models.DateTimeField(default=timezone.now)
    DateUpdated = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = "s_province"
        verbose_name = '省份'  
        verbose_name_plural = verbose_name
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class S_City(models.Model):
    CityID = models.AutoField("CityID",primary_key=True)
    CityName = models.CharField(max_length=100)
    ZipCode = models.CharField(max_length=100)
    Province = models.ForeignKey(S_Province, db_column="ProvinceID")
    DateCreated = models.DateTimeField(default=timezone.now)
    DateUpdated = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = "s_city"
        verbose_name = '市'  
        verbose_name_plural = verbose_name
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
    
    
class S_District(models.Model):
    DistrictID = models.AutoField("DistrictID",primary_key=True,)
    DistrictName = models.CharField(max_length=100)
    City = models.ForeignKey(S_City, db_column="CityID")
    DateCreated = models.DateTimeField(default=timezone.now)
    DateUpdated = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = "s_district"
        verbose_name = '区'
        verbose_name_plural = verbose_name
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
    
    
