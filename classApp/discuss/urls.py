from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'discuss'

urlpatterns = [
    path('create-post/', views.create_post, name='add-post'),
    path('forum/', views.forum_home, name='forum-home'),
    path('post/<post_id>', views.post_detail, name='post-detail'),
    path('add-reply/<post_id>', views.add_reply, name='add-reply'),
]
