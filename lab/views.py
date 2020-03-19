from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from reportlab.lib.pagesizes import A4, letter

from .Serializers import *
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template.loader import get_template
from django.db.models import Q
from .utils import render_to_pdf
from django.views.generic import View

class PatientAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        patient = Patient.objects.all()
        patients_serializer = PatientSerializer(patient, many=True, context={'request': request})
        return Response(patients_serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InsuranceAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        name = Insurance.objects.all()
        Insurance_serializer = InsuranceSerializer(name, many=True, context={'request': request})
        return Response(Insurance_serializer.data)

    def post(self, request):
        serializer = InsuranceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        tests = Test.objects.all()
        Test_serializer = TestSerializer(tests, many=True, context={'request': request})
        return Response(Test_serializer.data)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def All_Labs(request):
    Borders = serialize('geojson', Lab.objects.all())
    return HttpResponse(Borders, content_type='json')


class HomePageView(TemplateView):
    template_name = 'index.html'



def All_Area(request):
    area = serialize('geojson', Area.objects.all())
    return HttpResponse(area, content_type='json')


class AreasView(TemplateView):
    template_name = 'areas.html'



#
# class SearchResultsView(ListView):
#     model = Lab
#     template_name = 'search_results.html'
#
#     def get_queryset(self): # new
#         query = self.request.GET.get('q')
#         result= Lab.objects.filter(Q(name__icontains=query))
#         return resulthttp://127.0.0.1:8000/price#

def search_by_city(request):  # new
    query = request.GET.get('q')
    value = list(Lab.objects.filter(Q(address__icontains=query)))
    v = list(Lab.objects.filter(Q(area__name_0__icontains=query)))
    all_data=[]
    all_data+=value

    for x in value:
        if value.__contains__(x):
            continue
        else:
            value.append(x)

    return render(request, template_name='search_results.html', context={
        "value": all_data
    })




def testGet(request):
    print('-------------------kkkkk--------------------------------------------------------')
    value = Test.objects.values()
    patients = Patient.objects.values()
    doctors=Doctor.objects.values()
    return render(request, template_name='prices.html', context={
        "tests": value,
        "patients": patients,
    })


buddy = User.objects.get(username='admin')
token = Token.objects.get(user=buddy)
print('-----------------Token :--------------------')
print(token.key)
print('-----------------Token :--------------------\n')
