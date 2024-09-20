from django.shortcuts import render,redirect
from student.models import Student_user
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def student_home(request):
    return render(request,'student_home.html')

def login_user(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_staff==True:
                login(request,user)
                return redirect('t_home')
            else:
                login(request,user)
            return redirect('s_home')
        else:
            messages.error(request,"Invalid user credentials")
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')

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

def student_admit_card(request):
    return render(request, 'student_admit_card.html') 

def stud_study_material(request):
    return render(request, 'stud_study_material.html') 

def student_exam(request):
    return render(request, 'student_exam.html') 

def student_result(request):
    return render(request, 'student_result.html') 

def student_seating_arrangement(request):
    return render(request, 'student_seating_arrangement.html') 


