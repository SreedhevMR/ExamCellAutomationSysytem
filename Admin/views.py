from django.shortcuts import render
from django.shortcuts import render, redirect
from student.models import Student_user 
from teacher.models import Teacher_user 

def admin_page(request):
    return render(request,'admin.html')

 
def admin_student(request):
    students = Student_user.objects.all()  # Fetch all students
    return render(request, 'admin_student.html', {'students': students})


def admin_teacher(request):
    teachers = Teacher_user.objects.all()  # Fetch all teachers
    return render(request, 'admin_teacher.html', {'teachers': teachers})

