from django.contrib import admin
from django.urls import path, include
from localdb import views

app_name = 'common_views'

urlpatterns = [
    path('home/', views.Homepage.as_view()),
    path('importance/',views.MinersImportance.as_view(),name='importanceof'),
    path('history/',views.MinersHistory.as_view(),name='history'),
    path('store/',views.MinersStore.as_view(),name='store')
]
