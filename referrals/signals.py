from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from referrals.models import Profile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
