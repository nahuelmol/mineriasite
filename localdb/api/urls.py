from django.contrib import admin
from django.urls import path

from rest_framework import routers

from localdb.api import views

app_name = 'myapi'

router = routers.DefaultRouter()

router.register(r'interprises', views.InterprisesView, basename='interprise')
router.register(r'minerals', views.MineralsView, basename='mineral')

urlpatterns = router.urls
