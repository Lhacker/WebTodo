from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'todo/login.html', {})

def do_login(request):
    return HttpResponse("do_login")

def index(request):
    return HttpResponse("index")
