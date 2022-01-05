from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    print("Handling request to home page.")
    return HttpResponse("Hello, Azure!")
