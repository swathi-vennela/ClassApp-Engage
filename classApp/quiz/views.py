from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from users.models import *
from .models import *
from users.decorators import *
from .forms import *

@login_required
@teacher_required
def create_quiz(request):
    if request.method == "POST":
        form = QuizForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.author = request.user 
            data.save()
            return redirect("quiz:quiz-home")

    else:
        form = QuizForm()
    return render(request, 'quiz/create_quiz.html', {"form" : form})

def quiz_home(request):
    return render(request, 'quiz/quiz_home.html', context={'quizzes' : Quiz.objects.all()})

@login_required
@teacher_required
def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id = quiz_id)

    context = {
        "quiz" : quiz,
    }
    return render(request, 'quiz/quiz_detail.html', context)

@login_required
@teacher_required
def add_question(request, quiz_id):
    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid():
            quiz = get_object_or_404(Quiz, id=quiz_id)
            data = form.save(commit=False)
            data.save()
            quiz.questions.add(data)
            url = "quiz/"+str(quiz_id)
            return redirect(reverse("quiz:quiz-detail",kwargs={'quiz_id':str(quiz_id)}))
    else:
        form = QuestionForm()
    return render(request, 'quiz/add_question.html', {"form" : form})

@login_required 
@student_required
def attempt_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        questions = quiz.questions.all()
        score = 0
        total=0
        wrong=0
        correct=0
        for q in questions:
            total += 1
            print(request.POST.get(q.ques_id))
            print(q.ans)
            if q.ans == request.POST.get(q.ques_id):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        context = {
            'score' : score,
            'correct' : correct,
            'wrong' : wrong,
            'percent' : percent,
            'total' : total,
        }
        return render(request, 'quiz/result.html', context)
    else:
        questions = quiz.questions.all()
        context = {
            'quiz' : quiz,
            'questions' : questions,
        }
        return render(request, 'quiz/attempt-quiz.html', context)


