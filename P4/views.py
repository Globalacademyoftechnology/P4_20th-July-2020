from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>Welcome To The Djnago Project</marquee>")

def demo1(request):
    return render(request,"first.html")

def demo2(request):
    return render(request,"directory/second.html")

def third(request):
    return render(request,"directory/third.html",context={"data":"1234","name":"Sneha Bhatt U"})

def fruits(request):
    fruits_val=["Apple","Mango","Jackfruit","Pineapple","Kiwi"]
    return render(request,"directory/fourth.html",context={"fruits":fruits_val})

def fifth(request):
    return render(request,"directory/fifth.html",context={"a":20,"b":70})


    