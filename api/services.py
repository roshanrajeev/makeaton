from api.models import Challenge, Post, User
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token

from api.selectors import get_token

def user_create(*, email: str, password: str, first_name: str, last_name: str) -> User:
    try:
        User.objects.get(email=email)
        raise ValidationError("User with this email already exists")
    except User.DoesNotExist:
        user = User.objects.create_user(
            email=email, 
            password=password, 
            first_name=first_name, 
            last_name=last_name
        )
        user.save()
        Token.objects.create(user=user)
        return user

def user_login(*, email: str, password: str) -> User:
    user = None
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise ValidationError("Username or password is incorrect")
    
    if not user.check_password(password):
        return ValidationError("Username or password is incorrect")

    return get_token(user=user)

def challenge_create(*, 
        user: User,
        name: str, 
        description: str, 
        insights: str, 
        point: str
    ) -> Challenge:
    challenge = Challenge.objects.create(
        name=name, 
        description=description,
        created_by=user, 
        insights=insights, 
        point=point
    )
    challenge.accepted_users.add(user)
    challenge.accepted_count += 1
    challenge.save()
    return challenge


def challenge_update(*, pk: int, user: User, **kwargs) -> Challenge:
    challenge = None
    try:
        challenge = Challenge.objects.get(id=pk)
    except Challenge.DoesNotExist:
        raise ValidationError("Challenge with this id does not exist")
    
    if challenge.created_by.id != user.id:
        raise ValidationError("You are not allowed to update this challenge")

    for key, value in kwargs.items():
        setattr(challenge, key, value)

    challenge.save()
    return challenge


def challenge_delete(*, pk: int) -> Challenge:
    challenge = None
    try:
        challenge = Challenge.objects.get(pk=pk)
    except Challenge.DoesNotExist:
        raise ValidationError("Challenge with this id does not exist")
    challenge.delete()
    return challenge


def challenge_accept(*, pk: int, user: User) -> Challenge:
    challenge = None
    try:
        challenge = Challenge.objects.get(pk=pk)
    except Challenge.DoesNotExist:
        raise ValidationError("Challenge with this id does not exist")
    
    if challenge.accepted_users.filter(id=user.id).exists():
        raise ValidationError("You have already accepted this challenge")

    challenge.accepted_users.add(user)
    challenge.accepted_count += 1
    challenge.save()
    return challenge


def post_create(*, user: User, challenge_id: int=None, image: str=None, text: str=None) -> Post:
    post = Post.objects.create(
        posted_by=user,
        text=text,
        image=image
    )
    if challenge_id:
        try:
            challenge = Challenge.objects.get(pk=challenge_id)
            post.related_challenge = challenge
        except Challenge.DoesNotExist:
            raise ValidationError("Challenge with this id does not exist")
            
    post.save()
    return post


def post_delete(*, pk: int) -> Post:
    post = None
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise ValidationError("Post with this id does not exist")
    post.delete()
    return post


def post_like(*, pk: int, user: User) -> Post:
    post = None
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise ValidationError("Post with this id does not exist")
    
    if post.liked_users.filter(id=user.id).exists():
        raise ValidationError("You have already liked this post")

    post.liked_users.add(user)
    post.likes_count += 1
    post.save()
    return post