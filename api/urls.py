from django.urls import include, path

from api.views import *

urlpatterns = [
    path("signup/", UserCreateApi.as_view(), name="signup"),
    path("login/", UserLoginApi.as_view(), name="login"),
    path("badge/<int:id>", Badgeapi.as_view(), name="badge"),

]
