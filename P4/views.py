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

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))


#Giving one single value as an output with a space between the numbers, tehn finding the summation of 2 numbers and returning back the result in str format. 

def ab(request,val):
    result=val.split(" ")
    add_val=int(result[0])+int(result[1])
    return HttpResponse(str(add_val))



#To add 2 numbers given in the URL as input

def summation(request,a,b):
    add=int(a)+int(b)
    return HttpResponse(str(add))


#To find the greatest of 2 integers

def greatest(request,number):                        
    val=number.split(" ")

    if int(val[0]) > int(val[1]):
        res=int(val[0])
    else:
        res=int(val[1])
    final=res
    return HttpResponse(str(final))


#Giving the string as input in the URL, display the number of vowels and consonants in the given string

def vowel_consonant(request,input):
    count1=0
    count2=0
    for j in input:
        if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
            count1=count1+1
        elif j==" ":
            continue
        else:
            count2=count2+1
    dict={}
    dict.setdefault("vowels", count1)
    dict.setdefault("consonants", count2)
    return HttpResponse(str(dict))



