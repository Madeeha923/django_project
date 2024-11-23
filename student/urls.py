from django.contrib import admin
from django.urls import path, include
from student import views
from student.views import *

urlpatterns = [
    path('', views.index, name="home"),
    path('user/',user),
    path('about/',about),
    path('services/',services),
    path('contact/', contact),
    # path('admin/student/Stdnt/add/',add)
    path('user/std/', std),
]