# med_center_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinic.urls')),
    path('api/', include('clinic.urls')),
]
