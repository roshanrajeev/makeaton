from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from api.models import Challenge, Post, User

def get_token(*, user: User) -> str:
    return Token.objects.get(user=user).key


def challenge_list() -> list:
    return Challenge.objects.all()


def challenge_detail(*, pk: int) -> Challenge:
    challenge = None
    try:
        challenge = Challenge.objects.get(pk=pk)
    except Challenge.DoesNotExist:
        raise ValidationError("Challenge with this id does not exist")
    return challenge


def post_list() -> list:
    return Post.objects.all()

def post_detail(*, pk: int) -> Post:
    post = None
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise ValidationError("Post with this id does not exist")
    return post