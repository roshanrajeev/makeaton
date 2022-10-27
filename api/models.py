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
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Badges(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    image = models.TextField(blank=False, null=False)
    unlock_point = models.IntegerField(blank=False, null=False)


class Challenge(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    accepted_count = models.IntegerField(default=0)
    accepted_users = models.ManyToManyField(User, related_name='accepted_challenges')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='challenges', blank=False, null=False)
    insights = models.CharField(max_length=200, blank=True, null=True)
    point = models.IntegerField(default=0, blank=False, null=False)


class Post(models.Model):
    image = models.TextField(blank=True, null=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    likes_count = models.IntegerField(default=0)
    liked_users = models.ManyToManyField(User, related_name='liked_posts')
    comment_count = models.IntegerField(default=0)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=False, blank=False)
    related_challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)


class Comment(models.Model):
    text = models.CharField(max_length=200, blank=False, null=False)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=False, blank=False)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=False, blank=False)


class Profile(models.Model):
    image = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', blank=False, null=False)
    reward_points = models.IntegerField(default=0)
    unlocked_badges = models.ManyToManyField(Badges, related_name='profiles')