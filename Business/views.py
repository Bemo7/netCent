from django.shortcuts import render #used to render a template and return HTML markup to the client
from django.http import HttpResponse

# Create your views here.
# a view function is a function that takes a request and returns a result. result -> response.
# this is request handler
# In some frameworks it's called an action but in Django it's called a view

# What this function can do:
    # Pull data from a db
    # Transform data
    # Send emails

def Home(request):
    return render(request, 'hello.html', {'name' : 'Everyone'})

def restricted(request):
    return HttpResponse('Nigga! The URL says RESTRICTED'.replace('URL','route'))


def Contact(request):
    return HttpResponse('The Contact page is under construction...')
