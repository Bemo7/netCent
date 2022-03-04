# Mapping urls to views
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.say_hello, name = "hello"),
    path('restricted/', views.restricted, name = "restricted")
]
