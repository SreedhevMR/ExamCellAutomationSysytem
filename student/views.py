from django.shortcuts import render, redirect
from student.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from teacher.models import Exam, Subject
from teacher.forms import StudyMaterialForm 
from teacher.models import StudyMaterial
from teacher.models import ExamResult,Exam

def index(request):
    return render(request, 'index.html')

def student_home(request):
    return render(request, 'student_home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('t_home')
            else:
                login(request, user)
                return redirect('s_home')
        else:
            messages.error(request, "Invalid user credentials")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')

def sign_choice(request):
    return render(request, 'signup_choice.html')

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
        
        user = User.objects.create_user(username=email, password=password)
        data = Student_user(
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
    return render(request, 'student_signup.html')

def student_admit_card(request):
    return render(request, 'student_admit_card.html')

def stud_study_material(request):
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('tchr_study_material')  # Adjust the redirect URL as per your project setup
    else:
        form = StudyMaterialForm()

    # Corrected: Query the StudyMaterial model, not the form
    materials = StudyMaterial.objects.all()

    return render(request, 'stud_study_material.html', {
        'form': form,
        'materials': materials,
    })


def student_exam(request):
    exams = Exam.objects.prefetch_related('subjects').all()

    if request.method == 'POST':
        exam_name = request.POST.get('exam_name')
        subjects_data = request.POST.getlist('subjects')
        codes_data = request.POST.getlist('codes')
        dates_data = request.POST.getlist('dates')

        exam = Exam.objects.create(name=exam_name)

        for subject_name, subject_code, subject_date in zip(subjects_data, codes_data, dates_data):
            Subject.objects.create(exam=exam, name=subject_name, code=subject_code, date=subject_date)

    return render(request, 'student_exam.html', {'exams': exams})

def student_result(request):
    # Fetch all exams for the dropdown
    exams = ExamName.objects.all()

    # Handle search query
    search_query = request.GET.get('search', '')  # Get the search term from the URL

    # If there's a search query, filter results by the student's name, and order by exam name and student name
    if search_query:
        results = ExamResult.objects.select_related('exam').filter(
            student_name__icontains=search_query
        ).order_by('exam__name', 'student_name')
    else:
        # If no search, show all results ordered by exam name and student name
        results = ExamResult.objects.select_related('exam').all().order_by('exam__name', 'student_name')

    if request.method == 'POST':
        exam_id = request.POST.get('exam')
        student_name = request.POST.get('student_name')
        score = request.POST.get('score')
        date = request.POST.get('date')

        # Create a new exam result
        ExamResult.objects.create(exam_id=exam_id, student_name=student_name, score=score, date=date)
        return redirect('student_result')  # Redirect to the same page after submission

    return render(request, 'student_result.html', {'results': results, 'exams': exams, 'search_query': search_query})

def student_seating_arrangement(request):
    return render(request, 'student_seating_arrangement.html')
