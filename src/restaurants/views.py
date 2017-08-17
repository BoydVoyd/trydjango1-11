from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    num = random.randint(0,10000)
    some_list = [num, random.randint(0,10000), random.randint(0,10000)]
    context = {
        "html_var":"rad", 
        "num":num, "bool_item":True, 
        "some_list": some_list
        }
    return render(request, "home.html", context)

def home2(request):
    num = random.randint(0,10000)
    some_list = [num, random.randint(0,10000), random.randint(0,10000)]
    context = {

        }
    return render(request, "home2.html", context)

def home3(request):
    num = random.randint(0,10000)
    some_list = [num, random.randint(0,10000), random.randint(0,10000)]
    context = {

        }
    return render(request, "home3.html", context)