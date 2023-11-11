from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1ofapp1(request):
    return render(request,'1html.html')
def fun2ofapp1(request):
    return HttpResponse('<h1><marquee>Hi I am FUNCTION1 Of APP1<marquee></h1>')

