from django.shortcuts import get_object_or_404, redirect, render
from users.models import *
from .models import *
from users.decorators import *
from .forms import *

@student_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            stud = get_object_or_404(Student, user=request.user)
            data = form.save(commit=False)
            data.user1 = request.user
            data.image = stud.student_profile_pic
            data.save()
            return redirect("discuss:forum-home")
    else:
        form = PostForm()
    return render(request, 'discuss/add_post.html', {"form":form})

def forum_home(request):
    return render(request, 'discuss/forum.html', context={'posts' : Post.objects.all().order_by("-timestamp")})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    #post = Post.objects.get(post_id=post_id)
    replies = Replie.objects.filter(post = post).order_by("-timestamp")
    context = {
        "replies" : replies,
        "post" : post,
    }
    return render(request, 'discuss/post_detail.html', context)

@student_required
def add_reply(request, post_id):
    if request.method == "POST":
        form = ReplyForm(request.POST)

        if form.is_valid():
            post = get_object_or_404(Post, id=post_id)
            stud = get_object_or_404(Student, user=request.user)
            data = form.save(commit=False)
            data.user = request.user
            data.post = post 
            data.image = stud.student_profile_pic
            data.save()
            return redirect("discuss:forum-home")
    else:
        form = ReplyForm()
    return render(request, 'discuss/add_reply.html', {"form" : form})



            

