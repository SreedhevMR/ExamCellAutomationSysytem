from django.db import models
from django.contrib.auth.models import User
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
    photo = models.ImageField(upload_to='media/',null=True)
    user=models.OneToOneField(User,related_name='teacher_profile',on_delete=models.CASCADE)

    def __str__(self):
        return self.name





class Exam(models.Model):
    name = models.CharField(max_length=255)
    # other exam fields

    def __str__(self):
        return self.name

class Subject(models.Model):
    exam = models.ForeignKey(Exam, related_name='subjects', on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)  # Add name field to represent subject name
    code = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.code})"

    



class StudyMaterial(models.Model):
    material_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_uploaded = models.DateField()
    pdf_file = models.FileField(upload_to='study_materials/')

    def __str__(self):
        return self.material_name

    class Meta:
        db_table = 'teacher_studymaterial'  


class ExamName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ExamResult(models.Model):
    exam = models.ForeignKey(ExamName, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    score = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student_name} - {self.exam.name}: {self.score}"
