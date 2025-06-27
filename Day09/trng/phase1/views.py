from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def lemon(request):
    temp=loader.get_template('G.html')
    return HttpResponse(temp.render())
def day1(request):
    temp=loader.get_template('mca.html')
    return HttpResponse(temp.render())
def day2(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())
def day3(request):
    temp=loader.get_template('mca.html')
    return HttpResponse(temp.render())
def day4(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())
def day5(request):
    temp=loader.get_template('mca.html')
    return HttpResponse(temp.render())
def day6(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())
def day7(request):
    temp=loader.get_template('a.html')
    return HttpResponse(temp.render())
def day8(request):
    temp=loader.get_template('mca.html')
    return HttpResponse(temp.render())
def day9(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())
def day10(request):
    temp=loader.get_template('a.html')
    return HttpResponse(temp.render())
def day11(request):
    temp=loader.get_template('mca.html')
    return HttpResponse(temp.render())
def day12(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())
def day13(request):
    temp=loader.get_template('a.html')
    return HttpResponse(temp.render())
def day14(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())
def day15(request):
    temp=loader.get_template('mca.html')
    return HttpResponse(temp.render())


# Create your views here.
