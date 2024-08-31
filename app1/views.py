from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def print_login(request):
    return render(request,'login.html')

def choice_signup(request):
    return render(request,'signup_choice.html')
