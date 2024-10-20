from django.db import models
from django.contrib.auth.models import User
from teacher.models import Subject
from django.db import models
from django.contrib.auth.models import User


class Student_user(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    sex = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    mobile = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='media/', null=True)
    user = models.OneToOneField(User, related_name='student_profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class ExamName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    



class Student_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    address = models.TextField()
    sex = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    def __str__(self):
        return self.name



