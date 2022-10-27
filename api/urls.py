from django.urls import include, path

from api.views import create_user

urlpatterns = [
    path("", create_user, name="create_user")
]