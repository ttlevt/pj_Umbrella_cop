#-*- coding: utf-8 -*-
from django.urls import path
from insert_place import views
urlpatterns = [
    path("",views.home, name=" home")
]