from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse


# Create your views here.
def first(request):
    return render(request,'example.html')
def second(request):
    return render(request,'second.html')
def main(request):
    return render(request,'main.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def store(request):
    return render(request,'store.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')

