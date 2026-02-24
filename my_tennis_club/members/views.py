from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("<h2>Hello world! hello webprog it242 </h2>")