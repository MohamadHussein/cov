
from django.contrib import admin
from django.urls import path
from lab.views import *
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/', PatientAPI.as_view()),
    path('test/', TestAPI.as_view()),
    path('insu/',InsuranceAPI.as_view()),
    url(r'^', include('lab.urls')),

]
