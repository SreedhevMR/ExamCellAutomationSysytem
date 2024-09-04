
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
  path('',views.index,name='index'),
  path('logiin_user',views.login_user,name='login_user'),
  path('choice/',views.sign_choice,name='signup_choice'),
  path('student_signup',views.student_signup,name='s_signup'),
  path('student_home',views.student_home,name='s_home'),
  path('logout/',views.logout_user,name='logout_user')
]


