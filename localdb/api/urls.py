from django.contrib import admin
from django.urls import path

from rest_framework import routers

from localdb.api import views

app_name = 'myapi'

router = routers.DefaultRouter()

router.register(r'interprises', views.InterprisesView, basename='interprise')
router.register(r'minerals', views.MineralsView, basename='mineral')
router.register(r'proyects', views.ProyectsView, basename='proyects')
router.register(r'regions',views.RegionsView, basename='regions')

urlpatterns = router.urls
