from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.errors import ApiErrorsMixin

from api.services import user_create, user_login

# Create your views here.
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

