from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def v1(request):
    return HttpResponse("<h1>Vista 1</h1>")

def v2(request):
    return HttpResponse("<h1>Vista 2 app2</h1>")