from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Student_user,Teacher_user
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
# Create your views here.


# def student_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Authenticate user
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             # Log the user in
#             login(request, user)
#             messages.success(request, 'Login successful!')
#             return redirect('home')  # Redirect to a successful login page or home
#         else:
#             messages.error(request, 'Invalid username or password.')
    
#     return render(request, 'student_login.html')



# def teacher_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Authenticate user
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             # Log the user in
#             login(request, user)
#             messages.success(request, 'Login successful!')
#             return redirect('home')  # Redirect to a successful login page or home
#         else:
#             messages.error(request, 'Invalid username or password.')
    
    # return render(request, 'login.html')

def choice_signup(request):
    return render(request,'signup_choice.html')

def print_login(request):
     return render(request,'student_login.html')

@csrf_protect
def student_signup(request):
    if request.method == 'POST':
        # Directly getting data from POST request
        name = request.POST['name']
        age = request.POST['age']
        department = request.POST['department']
        address = request.POST['address']
        sex = request.POST['sex']
        mobile = request.POST['mobile']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        photo = request.FILES.get('photo')
       
        # Create a new user profile with the data
        student_profile = Student_user(
            name=name,
            age=age,
            department=department,
            address=address,
            sex=sex,
            mobile=mobile,
            email=email,
            username=username,
            password=password,  # Remember to hash this password securely
            photo=photo,
            
        )
        
        # Save the user profile
        student_profile.save()
        return redirect('login')
    
    return render(request, 'student_signup.html')

def teacher_signup(request):
    if request.method == 'POST':
        # Directly getting data from POST request
        name = request.POST['name']
        age = request.POST['age']
        department = request.POST['department']
        address = request.POST['address']
        sex = request.POST['sex']
        mobile = request.POST['mobile']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        photo = request.FILES.get('photo')

        # Create a new user profile with the data
        teacher_profile = Teacher_user(
            name=name,
            age=age,
            department=department,
            address=address,
            sex=sex,
            mobile=mobile,
            email=email,
            username=username,
            password=password,  # Remember to hash this password securely
            photo=photo
    
        )
        
        # Save the user profile
        teacher_profile.save()
        return redirect('login')

    return render(request,'teacher_signup.html')

def ahome(request):
    return render(request, 'ahome.html')