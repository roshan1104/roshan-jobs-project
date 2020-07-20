from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobsinfo(request):
    s="<h1>Hyderabad Jobs information</h1>"
    return HttpResponse(s)
def punjobsinfo(request):
    s="<h1>Pune Jobs information</h1>"
    return HttpResponse(s)
