from django.contrib import admin
from django.urls import path
from task1 import views as task1_views
from task3 import views as task3_views
from task4 import views as task4_views
from task5 import views as task5_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', task1_views.index, name='index'),
    path('task1/', task1_views.task1, name='task1'),
    path('task3/', task3_views.task3, name='task3'),
    path('task4/', task4_views.task4, name='task4'),
    path('task5/', task5_views.task5, name='task5'),
]
