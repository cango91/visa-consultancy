from django.contrib import admin
from .models import AppUser, UserProfile

# Register your models here.

admin.site.register(AppUser)
admin.site.register(UserProfile)