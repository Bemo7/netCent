# Mapping urls to views
from django.urls import path
from . import views
from .views import inventory_list
# URLConf
urlpatterns = [
    path('', views.say_hello, name = "hello"),
    path('list/', inventory_list, name="inventory_list" )
]
