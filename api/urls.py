from django.urls import include, path

from api.views import *

urlpatterns = [
    path("signup/", UserCreateApi.as_view(), name="signup"),
    path("login/", UserLoginApi.as_view(), name="login"),

    # CHALLENGES CRUD
    path("challenges/", ChallengeListApi.as_view(), name="challenge_list"),
    path("challenges/<int:pk>/", ChallengeDetailApi.as_view(), name="challenge_detail"),
    path("challenges/create/", ChallengeCreateApi.as_view(), name="challenge_create"),
    path("challenges/<int:pk>/update/", ChallengeUpdateApi.as_view(), name="challenge_update"),
    path("challenges/<int:pk>/delete/", ChallengeDeleteApi.as_view(), name="challenge_delete"),
    path("challenges/<int:pk>/accept/", ChallengeAcceptApi.as_view(), name="challenge_accept"),

    # POSTS CRUD
    path("posts/", PostListApi.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailApi.as_view(), name="post_detail"),
    path("posts/create/", PostCreateApi.as_view(), name="post_create"),
    path("posts/<int:pk>/delete/", PostDeleteApi.as_view(), name="post_delete"),
    path("posts/<int:pk>/like/", PostLikeApi.as_view(), name="post_like"),
    
    # yolo
    path('detect/',yoloyoyo.as_view(),name='object_detection'),
    #gpt3
    path('insights/<str:label>/',gpt3.as_view(),name='gpt3_view'),


]
