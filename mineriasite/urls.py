from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('localdb.api.urls',namespace='myapi')),
    path('',include('localdb.urls', namespace='common_views'))
]
