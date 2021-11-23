from django.db import models
from users.models import User
from django.utils.timezone import now
from django.urls import reverse

class Post(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_id = models.AutoField
    #slug = models.SlugField(unique=True)
    post_content = models.TextField()
    timestamp= models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images",default="")

    def get_absolute_url(self):
        #id_str = ""+self.post_id
        return reverse("discuss:post-detail", kwargs={
            'post_id' : self.id
        })
    def get_reply_item_url(self):
        return reverse("discuss:add-reply", kwargs={
            'post_id' : self.id 
        })
    
class Replie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reply_id = models.AutoField
    reply_content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    timestamp= models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images",default="")