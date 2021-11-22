from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'users'

urlpatterns = [
    path("", views.index_view, name='home'),
    path('student_register/',views.stud_register.as_view(),name='student_register'),
    path('teacher_register/',views.teacher_register.as_view(),name='teacher_register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
