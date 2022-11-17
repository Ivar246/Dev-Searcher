from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile
  
# @receiver(post_save, sender=Profile)
def createPeofile(sender, instance, created, **kwargs):
    print("profile signal triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=f'{user.first_name}'+ f'{user.last_name}'
        )
    


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createPeofile, sender=User)


post_delete.connect(deleteUser, sender=Profile)
