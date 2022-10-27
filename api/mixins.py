from rest_framework.permissions import IsAuthenticated
from api.auth import TokenAuthentication


class ApiAuthMixin:
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )