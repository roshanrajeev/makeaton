import openai
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.errors import ApiErrorsMixin
from api.mixins import ApiAuthMixin
from api.services import challenge_accept, challenge_create, challenge_delete, challenge_update, user_create, user_login
from api.selectors import challenge_detail, challenge_list
from api.models import *
from makeaton.settings import API_KEY


# print(API_KEY)
def generate_funfact_eq(text):


    prmt ="The carbon footprint on average left by a "+text+" is [insert] grams, That is equivalent to CO2 cleaned by [insert] trees in one night Or if it is made into a bubble, the size of the bubble will be equivalent to [insert object].\n"
    # print(prmt)
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prmt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    return response.choices[0].text


def generate_list_of_facts(text):


    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="List of unknown facts about a "+text+" based on history, carbon emission, innovation and future impact in India:\n",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    return response.choices[0].text


def generate_alternatives(text):


    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="List of green alternatives or improvements for a "+text+" ",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    return response.choices[0].text


# USER CRUD
class UserCreateApi(ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()
        first_name = serializers.CharField()
        last_name = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class UserLoginApi(ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        token = user_login(**serializer.validated_data)
        return Response(data={"token": token}, status=status.HTTP_200_OK)




# CHALLENGES CRUD
class ChallengeListApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Challenge
            fields = ["id", "name", "description", "accepted_count", "insights", "point"]

    def get(self, request):
        challenges = challenge_list()
        serializer = self.OutputSerializer(challenges, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ChallengeCreateApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=True)
        description = serializers.CharField(required=True)
        insights = serializers.CharField(required=True)
        point = serializers.IntegerField(required=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        challenge_create(user=request.user, **serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class ChallengeDetailApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Challenge
            fields = ["id", "name", "description", "accepted_count", "insights", "point"]

    def get(self, request, pk):
        challenge = challenge_detail(pk=pk)
        serializer = self.OutputSerializer(challenge)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ChallengeUpdateApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        description = serializers.CharField(required=False)
        insights = serializers.CharField(required=False)
        point = serializers.IntegerField(required=False)

    def put(self, request, pk):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        challenge_update(pk=pk, user=request.user, **serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

    
class ChallengeDeleteApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    def delete(self, request, pk):
        challenge_delete(pk=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChallengeAcceptApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    def post(self, request, pk):
        challenge_accept(pk=pk, user=request.user)
        return Response(status=status.HTTP_200_OK)