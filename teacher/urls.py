
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
  path('tacher_signup',views.teacher_signup,name='t_signup'),
  path('teacher_home',views.teacher_home,name='t_home'),
  path('tchr_study_material', views.tchr_study_material, name='t_material'),

]


