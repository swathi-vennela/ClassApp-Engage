from django.http.response import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from users.decorators import *
from .forms import *
from .models import *
from discuss.models import *
from quiz.models import * 

def index_view(request):
    return render(request, 'discuss/forum.html', context={'posts' : Post.objects.all()})
    #return render(request, 'users/home1.html')

class stud_register(CreateView):
    model = User
    form_class = StudentRegistrationForm
    template_name = 'users/student_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('/')


class teacher_register(CreateView):
    model = User
    form_class = TeacherRegistrationForm
    template_name = 'users/teacher_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('/')

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")

    return render(request,'users/login.html',context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
@student_required 
def student_profile(request):
    student = Student.objects.get(user = request.user)
    response_sheets = ResponseSheet.objects.filter(student=request.user)
    context = {
        "student" : student,
        "response_sheets" : list(response_sheets),
    }
    return render(request, 'users/student-profile.html', context)

@login_required
@teacher_required
def teacher_profile(request):
    teacher = Teacher.objects.get(user=request.user)
    quizzes = Quiz.objects.filter(author=request.user)
    context = {
        "teacher" : teacher,
        "quizzes" : list(quizzes),
    }
    return render(request, 'users/teacher-profile.html', context)

@login_required
@teacher_required
def quiz_responses(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    response_qs = ResponseSheet.objects.filter(quiz=quiz)
    context = {
        "quiz" : quiz,
        "responses" : list(response_qs),
    }
    return render(request, 'users/quiz_responses.html', context)

@login_required
def view_response_sheet(request, resp_id):
    response_sheet = ResponseSheet.objects.get(id = resp_id)
    user = response_sheet.student
    responses = response_sheet.responses.all()
    context = {
        "student" : user,
        "responses" : responses,
    }
    return render(request, 'users/view_response_sheet.html', context)