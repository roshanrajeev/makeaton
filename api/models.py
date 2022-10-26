from email.policy import default
from unicodedata import name
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager



# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    reward_points = models.PositiveIntegerField(default=0)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Badges(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.TextField()
    unlock_point = models.IntegerField()

    
class Community(models.Model):
    image = models.CharField(max_length=100)
    description = models.TextField()
    liked = models.PositiveIntegerField(default=0)
    likedby = models.ManyToManyField(User, related_name='likedby')
    postedby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postedby')
    comment_count = models.PositiveIntegerField(default=0)
    commentedby = models.ManyToManyField(User, related_name='commentedby')
    created_at = models.DateTimeField(auto_now_add=True)

class Challenges(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    days = models.IntegerField()
    points = models.IntegerField()
    challengedby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='createdby')
    created_at = models.DateTimeField(auto_now_add=True)
    joinedby = models.ManyToManyField(User, related_name='joinedby')
    completedby = models.ManyToManyField(User, related_name='completedby')


class ChallengeDetails(models.Model):
    challenge = models.ForeignKey(Challenges, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()

