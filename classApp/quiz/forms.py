from django import forms
from django.db.models import fields
from .models import *

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name','desc',)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('desc','choice1', 'choice2', 'choice3', 'choice4', 'ans')