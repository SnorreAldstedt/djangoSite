from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hei, dette er min test polls index")
# Create your views here.
