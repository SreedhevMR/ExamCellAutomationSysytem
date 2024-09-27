
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
  path('tacher_signup',views.teacher_signup,name='t_signup'),
  path('teacher_home',views.teacher_home,name='t_home'),
  path('teacher_student',views.teacher_student,name='t_student'),
  path('teacher_exam_hall',views.teacher_exam_hall,name='t_exam_hall'),
  path('teacher_seating_arrangement',views.teacher_seating_arrangement,name='t_arrangement'),
  path('teacher_offexam', views.teacher_offexam, name='t_offexam'),
  path('teacher_student',views.teacher_student,name='t_student'),
  path('tchr_study_material', views.tchr_study_material, name='t_material'),
  path('teacher_result', views.teacher_result, name='t_result'),
]


