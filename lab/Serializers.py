from .models import *
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['patient_ID','Salutation','first_name','middle_initial','middle_name','surname','gender','birth_date','lab']


class InsuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insurance
        fields = ['name']


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ['id','name','max_1995','min_1995','min_price','max_2008','jam']