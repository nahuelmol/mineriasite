from django.contrib import admin
from django.urls import path, include
from localdb import views

app_name = 'common_views'

urlpatterns = [
    path('home/', views.Homepage.as_view())
]
