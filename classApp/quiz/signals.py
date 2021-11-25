from django.db.models.signals import pre_delete
from django.conf import settings
from .models import *
from django.dispatch import receiver


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()

@receiver(pre_delete, sender=ResponseSheet)
def pre_delete_responsesheet(sender, instance, **kwargs):
    for res in instance.responses.all():
        res.delete()

@receiver(pre_delete, sender=Quiz)
def pre_delete_quiz(sender, instance, **kwargs):
    for ques in instance.questions.all():
        ques.delete()
        
