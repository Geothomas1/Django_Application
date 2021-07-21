from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello Welcome to Poll apps")
# Create your views here.
