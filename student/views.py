from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def login_user(request):
    return render(request,'login.html')

def sign_choice(request):
    return render(request,'signup_choice.html')

def student_signup(request):
    return render(request,'student_signup.html')
