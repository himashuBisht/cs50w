import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello!,check /brian")
    return render(request, "hello/index.html")


def brian(request):
    return HttpResponse("Hello,Brian")

#what is we want make it give output as of user input
def greet0(request, name):
    return HttpResponse(f"Hello ...  {name.capitalize()}!")

#render a page
def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})
