from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login

# Create your views here.
def index (request):
    return render (request,'Elearning.html')

def dashboard (request):
        return render (request,'Dashboard.html')



