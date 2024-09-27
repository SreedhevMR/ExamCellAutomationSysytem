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
    photo = models.ImageField(upload_to='media/',null=True)
    user=models.OneToOneField(User,related_name='student_profile',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    from django.db import models

class Exam(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    exam = models.ForeignKey(Exam, related_name='subjects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

    


