from api.models import Challenge, User
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