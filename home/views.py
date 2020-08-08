from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    return redirect('/')