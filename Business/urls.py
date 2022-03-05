# Mapping urls to views
from django.urls import path
from . import views
from .views import inventory_list
# URLConf
urlpatterns = [
<<<<<<< HEAD
    path('hello/', views.say_hello, name = "hello"),
    path('restricted/', views.restricted, name = "restricted"),
    path('', inventory_list, name="inventory_list" )
]
=======
    path('', views.say_hello, name = "hello"),
    path('restricted/', views.restricted, name = "restricted")
]
>>>>>>> bef10505c224aacb477889633a7b5560abdfcb7d
