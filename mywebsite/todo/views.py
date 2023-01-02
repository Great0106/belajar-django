from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Ini adalah halaman utama todo")

def title(request):
    return HttpResponse("<h1>ini adalah halaman title</h1>")
