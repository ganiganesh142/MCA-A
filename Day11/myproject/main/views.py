from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    temp=loader.get_template('home.html')
    return HttpResponse(temp.render())
def about(request):
    temp=loader.get_template('about.html')
    return HttpResponse(temp.render())
# Create your views here.
