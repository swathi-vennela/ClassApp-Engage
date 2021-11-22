from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

BRANCH_CHOICES = (
    ('CSE', 'Computer Science'),
    ('ECE', 'Electronics'),
    ('BIO', 'Bio-medical'),
    ('DSE','Datascience'),
    ('GEN','Generic')
)

class User(AbstractUser):
    email = models.EmailField()
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    stud_name = models.CharField(max_length=30)
    email = models.EmailField(default="")
    branch = models.CharField(choices=BRANCH_CHOICES, max_length =3, default = 'GEN')
    student_profile_pic = models.ImageField(default='img.png', upload_to='profile_pics', blank=True)

    def get_absolute_url(self):
        return reverse('/student', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    teacher_name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField(default = "")
    teacher_profile_pic = models.ImageField(default='img.png',upload_to = 'profile_pics',blank=True)
    #qualif = models.TextField()
    designation = models.CharField(max_length=300)
    branch = models.CharField(choices=BRANCH_CHOICES, max_length =3, default = 'GEN')
    def get_absolute_url(self):
        return reverse('/teacher',kwargs={'pk':self.pk})


    def __str__(self):
        return self.teacher_name

