from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>Welcome To The Djnago Project</marquee>")

def demo1(request):
    return render(request,"first.html")

def demo2(request):
    return render(request,"directory/second.html")
    