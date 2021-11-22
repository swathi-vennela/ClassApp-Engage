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
    return render(request, 'discuss/forum.html', context={'posts' : Post.objects.all()})

# def create_post(request):
#     profile = Student.objects.all()
#     if request.method=="POST":   
#         user = request.user
#         image = request.user.student_profile_pic
#         content = request.POST['post_content']
#         post = Post(user1=user, post_content=content, image=image)
#         post.save()
#         # alert = True
#         # return render(request, "forum.html", {'alert':alert})
#     posts = Post.objects.all()
#     return render(request, "discuss/forum.html", {'posts':posts})