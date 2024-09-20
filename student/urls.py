
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
  path('',views.index,name='index'),
  path('logiin_user',views.login_user,name='login_user'),
  path('choice/',views.sign_choice,name='signup_choice'),
  path('student_signup',views.student_signup,name='s_signup'),
  path('student_home',views.student_home,name='s_home'),
  path('student_admit_card', views.student_admit_card, name='s_card'),
  path('stud_study_material', views.stud_study_material, name='s_material'),
  path('student_exam', views.student_exam, name='s_exam'),
  path('student_result', views.student_result, name='s_result'),
  path('student_seating_arrangement', views.student_seating_arrangement, name='s_arrangement'),
  path('logout/',views.logout_user,name='logout_user'),
  

]


