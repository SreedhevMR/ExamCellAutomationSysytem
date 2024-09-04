
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
  path('tacher_signup',views.teacher_signup,name='t_signup')
]


