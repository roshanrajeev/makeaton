from django.urls import include, path

from api.views import UserCreateApi, UserLoginApi

urlpatterns = [
    path("signup/", UserCreateApi.as_view(), name="signup"),
    path("login/", UserLoginApi.as_view(), name="login"),
]