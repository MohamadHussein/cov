from django.contrib.gis.db import models
from django.contrib.gis.db.models import PointField as PField
from django.contrib.auth.models import User
from django import forms
from django.conf import settings

class Area(models.Model):
    id_0 = models.BigIntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.BigIntegerField()
    name_1 = models.CharField(max_length=75)
    type_1 = models.CharField(max_length=50)
    engtype_1 = models.CharField(max_length=50)
    nl_name_1 = models.CharField(max_length=50,null=True)
    varname_1 = models.CharField(max_length=150,null=True)
    population=models.IntegerField(null=True)
    confirmed_cases=models.IntegerField(null=True)
    geom = models.MultiPolygonField(srid=4326)
    def __str__(self):
        return self.name_1

class Lab(models.Model):
    manager=models.CharField(max_length=500,null=True)
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=100)
    area=models.ForeignKey(Area,on_delete=models.CASCADE,null=True,blank=True,)
    point_type=models.CharField(max_length=250,null=True)
    location=PField(null=True)

    def __str__(self):
        return self.name

class Insurance(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Patient(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    patient_ID=models.IntegerField()
    Salutation=models.CharField(null=True,blank=True,max_length=150)
    first_name=models.CharField(max_length=150)
    middle_initial=models.CharField(null=True,blank=True,max_length=150)
    middle_name=models.CharField(null=True,blank=True,max_length=150)
    surname=models.CharField(max_length=150)
    gender=models.CharField(max_length=100)
    birth_date=models.DateField(null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    country=models.CharField(max_length=150,null=True,blank=True)
    state=models.CharField(max_length=150)
    address=models.CharField(null=True,blank=True,max_length=150)
    insurance_company=models.ForeignKey(Insurance,null=True,blank=True,on_delete=models.CASCADE)
    insurance_Number=models.IntegerField()
    lab=models.ManyToManyField(Lab)
    def __str__(self):
        return self.first_name


class Doctor(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    Doctor_ID=models.IntegerField()
    name=models.CharField(max_length=150)
    gender=models.CharField(max_length=100)
    birth_date=models.DateField(null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    lab=models.ManyToManyField(Lab)
    address=models.CharField(null=True,blank=True,max_length=150)
    location=models.PointField(null=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=500)
    max_1995=models.IntegerField()
    min_1995=models.IntegerField()
    min_price=models.IntegerField()
    max_2008=models.IntegerField()
    jam=models.IntegerField()
    def __str__(self):
        return self.name

class Reports(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500)
    file = models.FileField(upload_to='',null=True)
#
# class city(models.Model):
#     id_0 = models.BigIntegerField()
#     iso = models.CharField(max_length=3)
#     name_0 = models.CharField(max_length=75)
#     id_1 = models.BigIntegerField()
#     name_1 = models.CharField(max_length=75)
#     type_1 = models.CharField(max_length=50)
#     engtype_1 = models.CharField(max_length=50)
#     nl_name_1 = models.CharField(max_length=50,null=True)
#     varname_1 = models.CharField(max_length=150,null=True)
#     geom = models.MultiPolygonField(srid=4326)
#

