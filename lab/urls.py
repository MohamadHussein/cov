from django.conf.urls import include,url
from .views import *

urlpatterns=[
    url(r'^Home/$',HomePageView.as_view(),name='home'),
    url(r'^areas/$', AreasView.as_view(), name='area'),
    url(r'^price/$', testGet, name='price'),
    url('search/', search_by_city, name='search_by_city'),
    url(r'^All_Labs/$', All_Labs, name='all'),
    url(r'^All_Areas/$', All_Area, name='areas'),


]