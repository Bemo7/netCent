# Mapping urls to views
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello, name = "hello"),
    path('restricted/', views.restricted, name = "restricted"),
    path('', views.Home, name = "Home")
]