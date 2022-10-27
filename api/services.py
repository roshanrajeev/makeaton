from api.models import User
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token

def user_create(*, email: str, password: str, first_name: str, last_name: str) -> User:
    try:
        User.objects.get(email=email)
        raise ValidationError("User with this email already exists")
    except User.DoesNotExist:
        user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        Token.objects.create(user=user)
        return user
    

def get_token(*, user: User) -> str:
    return Token.objects.get(user=user).key

def user_login(*, email: str, password: str) -> User:
    user = None
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise ValidationError("Username or password is incorrect")
    
    if not user.check_password(password):
        return ValidationError("Username or password is incorrect")

    return get_token(user=user)