from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import UserProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver function to save the userprofile instance after it's associated
    user instance is saved. This is needed to ensure that the userprofile instance is
    updated correctly when the user instance is updated.
    """

    instance.userprofile.save()

