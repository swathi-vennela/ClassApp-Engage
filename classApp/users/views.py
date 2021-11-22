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

def index_view(request):
    return render(request, 'users/home.html')
    #return HttpResponse('<h1>This is home page</h1>')

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