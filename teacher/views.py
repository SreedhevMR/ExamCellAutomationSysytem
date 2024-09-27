from django.shortcuts import render,redirect
from teacher.models import Teacher_user
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from .models import Exam, Subject  

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

def teacher_student(request):
    return render(request, 'teacher_student.html') 

def teacher_exam_hall(request):
    return render(request, 'teacher_exam_hall.html') 

def teacher_seating_arrangement(request):
    return render(request, 'teacher_seating_arrangement.html')

def teacher_exam(request):
     return render(request, 'teacher_exam.html') 

from django.shortcuts import render, get_object_or_404
from .models import Exam, Subject

def teacher_offexam(request):
    exams = Exam.objects.prefetch_related('subjects').all()

    if request.method == 'POST':
        exam_name = request.POST.get('exam_name')
        subjects_data = request.POST.getlist('subjects')
        codes_data = request.POST.getlist('codes')
        dates_data = request.POST.getlist('dates')

        exam = Exam.objects.create(name=exam_name)

        for subject_name, subject_code, subject_date in zip(subjects_data, codes_data, dates_data):
            Subject.objects.create(exam=exam, name=subject_name, code=subject_code, date=subject_date)

    return render(request, 'teacher_offline_exam.html', {'exams': exams})



def tchr_study_material(request):
    return render(request, 'tchr_study_material.html')
 
def teacher_result(request):
    return render(request, 'teacher_result.html') 