from django.shortcuts import render,redirect
from student.models import Student_user
from django.contrib.auth.models import User


def index(request):
    return render(request,'index.html')

def login_user(request):
    return render(request,'login.html')

def sign_choice(request):
    return render(request,'signup_choice.html')

def student_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        department = request.POST.get('department')
        address = request.POST.get('address')
        sex = request.POST.get('sex')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        photo = request.FILES.get('photo')
        user=User.objects.create_user(username=email,password=password)
        data=Student_user(
                name=name,
                age=age,
                department=department,
                address=address,
                sex=sex,
                mobile=mobile,
                email=email,
                photo=photo,
                user=user
                )
        data.save()
        return redirect('login_user')
    return render(request,'student_signup.html')




