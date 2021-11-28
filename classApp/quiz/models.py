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
    def get_attempt_url(self):
        return reverse("quiz:attempt-quiz", kwargs={
            'quiz_id' : self.id 
        })
    def get_responses_url(self):
        return reverse("users:quiz_responses", kwargs={
            'quiz_id' : self.id 
        })

class Response(models.Model):
    response_id = models.AutoField
    choice_picked = models.CharField(max_length=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class ResponseSheet(models.Model):
    resp_id = models.AutoField
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    responses = models.ManyToManyField(Response)
    score = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.quiz.name} of {self.id}"
    def get_response_sheet_url(self):
        return reverse("users:view_response_sheet", kwargs={
            'resp_id' : self.id 
        })


