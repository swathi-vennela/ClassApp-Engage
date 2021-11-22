from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import *

CHOICES = [
    ('CSE', 'Computer Science'),
    ('ECE', 'Electronics'),
    ('BIO', 'Bio-medical'),
    ('DSE','Datascience'),
    ('GEN','Generic')
]

class StudentRegistrationForm(UserCreationForm):
    email = forms.CharField(required=True)
    stud_name = forms.CharField(required=True)
    #branch = forms.Select(choices=CHOICES)
    branch = forms.CharField(label='Branch', widget=forms.Select(choices=CHOICES))
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.email=self.cleaned_data.get('email')
        user.save()
        student = Student.objects.create(user=user)
        student.email = self.cleaned_data.get('email')
        student.stud_name = self.cleaned_data.get('stud_name')
        student.branch = self.cleaned_data.get('branch')
        student.save()
        return user


class TeacherRegistrationForm(UserCreationForm):
    email = forms.CharField(required=True)
    teacher_name = forms.CharField(required=True)
    contact_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)
    branch = forms.CharField(label='Branch', widget=forms.Select(choices=CHOICES))
    class Meta(UserCreationForm.Meta):
        model = User  

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher=True
        user.email=self.cleaned_data.get('email')
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.teacher_name=self.cleaned_data.get('teacher_name')
        teacher.designation = self.cleaned_data.get('designation')
        teacher.contact_number=self.cleaned_data.get('contact_number')
        teacher.branch = self.cleaned_data.get('branch')
        teacher.email=self.cleaned_data.get('email')
        teacher.save()
        return user 