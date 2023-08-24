from allauth.socialaccount.signals import pre_social_login
from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import AppUser, UserProfile

@receiver(user_signed_up)
def check_social(request,user,**kwargs):
    try:
        socialuser = SocialAccount.objects.get(user_id=user.id)
        user.name = user.name or socialuser.extra_data['given_name']
        user.last_name = user.last_name or socialuser.extra_data['family_name']
        user.googleId = user.googleId or socialuser.uid
        user.email = user.email or socialuser.extra_data['email']
        user.save()
    except ObjectDoesNotExist as e:
        pass
    
@receiver(post_save,sender=get_user_model())
def create_profile(sender, instance=None, created=False,**kwargs):
    if created:
        UserProfile.objects.create(user=instance, role = 'customer' if not instance.is_superuser else 'employee')
        instance.profile.save()