from django.db import models

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
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)  # Use a secure method to handle passwords
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.username

from django.db import models

class Teacher_user(models.Model):
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
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128, default='defaultpassword')  # Set a default value
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, default="image")

    def __str__(self):
        return self.username