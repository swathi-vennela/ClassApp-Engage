from django import forms
from django.db.models import fields
from .models import *

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('post_content',)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Replie 
        fields = ('reply_content',)