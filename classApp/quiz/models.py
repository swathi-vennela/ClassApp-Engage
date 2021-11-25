from django.db import models
from users.models import Teacher, User
from django.utils.timezone import now
from django.urls import reverse

class Question(models.Model):
    ques_id = models.AutoField 
    desc = models.CharField(max_length=300)
    choice1 = models.CharField(max_length=40)
    choice2 = models.CharField(max_length=40)
    choice3 = models.CharField(max_length=40)
    choice4 = models.CharField(max_length=40)
    ans = models.CharField(max_length=1)

class Quiz(models.Model):
    quiz_id = models.AutoField
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    questions = models.ManyToManyField(Question)
    is_saved = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
    def get_absolute_url(self):
        return reverse("quiz:quiz-detail", kwargs={
            'quiz_id' : self.id 
        })
    def get_add_ques_url(self):
        return reverse("quiz:add-question", kwargs={
            'quiz_id' : self.id 
        })

