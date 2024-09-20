from django.shortcuts import render,redirect
from teacher.models import Teacher_user
from django.contrib.auth.models import User

def teacher_signup(request):
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
        user=User.objects.create_user(username=email,password=password,is_staff=True)
        data=Teacher_user(
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
    return render(request,'teacher_signup.html')

def teacher_home(request):
    return render(request,'teacher_home.html')

def tchr_study_material(request):
    return render(request, 'tchr_study_material.html') 
