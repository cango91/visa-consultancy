from allauth.socialaccount.signals import pre_social_login
from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from .models import AppUser

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