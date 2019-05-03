from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {'title': "Sample App Home Page"}
    return render(request, "sample_app/home.html", context)

def about(request):
    return render(request, "sample_app/about.html", {'title': "About Page"})

