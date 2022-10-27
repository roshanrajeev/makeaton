from rest_framework.authtoken.models import Token
from api.models import User

def get_token(*, user: User) -> str:
    return Token.objects.get(user=user).key