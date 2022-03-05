# Mapping urls to views
from django.urls import path
from . import views
from .views import inventory_list
# URLConf
urlpatterns = [
    path('hello/', views.say_hello, name = "hello"),
    path('restricted/', views.restricted, name = "restricted"),
    path('', inventory_list, name="inventory_list" )
<<<<<<< HEAD
]
=======
]
>>>>>>> 8cfda1699cb8ca5a94b7bb41b31f7812acba9f4e
