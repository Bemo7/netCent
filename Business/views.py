from multiprocessing import context
from django.shortcuts import render #used to render a template and return HTML markup to the client
from django.http import HttpResponse
from .models import Inventory


# Create your views here.
# a view function is a function that takes a request and returns a result. result -> response.
# this is request handler
# In some frameworks it's called an action but in Django it's called a view

# What this function can do:
    # Pull data from a db
    # Transform data
    # Send emails

def inventory_list(request):
    inventories = Inventory.objects.all() #Returns all inventories in the database
    context = {
        "title" : "Inventory List",
        "inventories" : inventories
    }
    return render(request, 'Inventory/inventory_list.html', context=context )

def say_hello(request):
    # Use "context" to create a title
    context = {
        "title": "TheFirst"
    }
    return render(request, 'hello.html', context=context )

def Home(request):
    return render(request, 'Inventory/index.html')

#def per_product_view(request, pk):
    