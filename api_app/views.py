from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from rest_framework import status
from .models import User, Role, Camera

from .serializers import (
    UserCreateSerializer, 
    UserLoginSerializer,
    UserProfileSerializer,
    RoleSerializer, 
    CameraSerializer, 
    ViewerSerializer)

from rest_framework import generics

from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


#user register
class UserRegister(generics.CreateAPIView):
    permission_classes= [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

#login
class UserLogin(APIView):
    permission_classes= [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data= request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data= serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
            
class UserProfile(generics.RetrieveUpdateAPIView):
    permission_classes= [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


class CameraList(generics.ListCreateAPIView):
    permission_classes= [AllowAny]
    queryset = Camera.objects.filter(uid=29).order_by('-created_at').exclude(cid=1)
    serializer_class = CameraSerializer

class CameraDetail(generics.ListAPIView):
    permission_classes= [AllowAny]
    queryset = Camera.objects.filter(uid=29)
    serializer_class = CameraSerializer


#get, post roles
class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

#get, update, delete role with role_id
#api/role/(?P<pk>[0-9]+)/ , put method need to have ending /
class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer  
   

# class Viewer(generics.ListCreateAPIView):
#     queryset = Viewer.objects.all()
#     serializer_class = ViewerSerializer
