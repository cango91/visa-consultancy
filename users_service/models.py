from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True) # Local authentication
    googleId = models.CharField(max_length=128, null=True) # Google oAuth
    name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128,blank=True)
    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female'),
        ('undisclosed','Do Not Want To Disclose'),
    )
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
class UserProfile(models.Model):
    user = models.OneToOneField(AppUser,on_delete=models.CASCADE,related_name='profile')
    USER_ROLES = (
        ('employee','Employee'),
        ('customer','Customer'),
    )
    role = models.CharField(max_length=12,choices=USER_ROLES)