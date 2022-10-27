from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.errors import ApiErrorsMixin
from api.mixins import ApiAuthMixin

from api.services import user_create, user_login
from .models import *
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

class Badgeapi(ApiAuthMixin,ApiErrorsMixin, APIView):
    '''
    authenticate with token and serialize inputs
    '''
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        description = serializers.CharField()
        image = serializers.CharField()
        unlock_point = serializers.IntegerField()
    
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        Badges.objects.create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
    
    def get(self,request,id):
        '''
        get badge with pk = id
        '''
        badge = Badges.objects.get(id=id)
        return Response(data=badge, status=status.HTTP_200_OK)

class Communityapi(ApiAuthMixin,ApiErrorsMixin, APIView):
    '''
    authenticate with token and serialize inputs
    '''


    class _InputSerializer(serializers.Serializer):
        class _UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('__all__',)
        image= serializers.CharField()
        description= serializers.CharField()
        liked = serializers.IntegerField()
        likedby = _UserSerializer(many=True)
        postedby = _UserSerializer()
        comment_count= serializers.IntegerField()
        commentedby = _UserSerializer(many=True)
        

    def post(self, request):
        serializer = self._InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Community.objects.create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

    def get(self,request,id):
        community = Community.objects.get(id=id)
        return Response(data=community, status=status.HTTP_200_OK)
    def delete(self,request,id):
        community = Community.objects.get(id=id)
        community.delete()
        return Response(status=status.HTTP_200_OK)