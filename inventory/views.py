from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        "title": "Bucket v01",
    }
    return render(request, "home.html", context)

def page1(request):
    context = {
        "title": "Bucket v01",
    }
    return render(request, "page1.html", context)