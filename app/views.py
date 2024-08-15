from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def firstView(req):
    return HttpResponse("This is the response from server by Sushil")